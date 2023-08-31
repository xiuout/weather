
# coding=utf-8
import turtle
from datetime import *
 
 
# 由于表盘刻度不连续，需频繁抬起画笔，放下画笔
def skip(step):
    turtle.penup()  # 画笔抬起
    turtle.forward(step)  # 画笔移动step
    turtle.pendown()  # 画笔落下
 
 
# 建立表针，定制表针形状和名字
def make_hand(name, length):
    turtle.reset()
 
    skip(-length * 0.1)  # 表针一端，过表盘中心一小段，开始绘制
    turtle.begin_poly()  # 开始记录多边形的第一个顶点。
    turtle.forward(length * 1.1)  # 设置表针长度，绘制表针
    turtle.end_poly()  # 停止记录多边形的顶点。当前的乌龟位置是多边形的最后一个顶点。将与第一个顶点相连。
 
    handForm = turtle.get_poly()  # 返回最后记录的形状
 
    turtle.color('black')
    turtle.register_shape(name, handForm)
 
 
# 三个表针初始化，实例化
def init_hand():
    global sec_hand, min_hand, hou_hand, printer
    # 重置Turtle指向北
    turtle.mode("logo")  # logo:向上（北） 顺时针   standard:向右（东）  逆时针
 
    # 建立三个表针Turtle并初始化
    make_hand("sec_Hand", 135)
    make_hand("min_Hand", 110)
    make_hand("hou_Hand", 70)
 
    sec_hand = turtle.Turtle()
    sec_hand.shape("sec_Hand")
    min_hand = turtle.Turtle()
    min_hand.shape("min_Hand")
    hou_hand = turtle.Turtle()
    hou_hand.shape("hou_Hand")
 
    # 笔的属性
    for hand in sec_hand, min_hand, hou_hand:
        hand.shapesize(1, 1, 3)
        hand.speed(0)
 
    # 建立输出打印的文字Turtle
    printer = turtle.Turtle()
 
    # 隐藏画笔的turtle形状
    printer.hideturtle()
    printer.penup()
 
 
# 设置表盘
def set_clock(radius):
    turtle.reset()
    turtle.pencolor('red')  # 设置画笔颜色
    turtle.fillcolor('pink')  # 设置绘制图形的填充颜色
    turtle.pensize(10)  # 画笔宽度
 
    for i in range(60):
        skip(radius)
        # 逢五 使用线条并加粗
        if i % 5 == 0:
            turtle.forward(20)
            skip(-radius - 20)
            skip(radius + 20)
 
            # 设置数字的位置及字体，大小
            if i == 0:
                turtle.write(int(12), align="center", font=("Courier", 14, "bold"))
            elif i == 30:
                skip(25)
                turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
                skip(-25)
            elif i == 25 or i == 35:
                skip(20)
                turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
                skip(-20)
            else:
                turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
            skip(-radius - 20)
        # 非五，以点代替
        else:
            turtle.dot(5)
            skip(-radius)
        turtle.right(6)
 
 
# 显示星期
def show_week(t):
    week = ["星期一  Mon", "星期二  Tue", "星期三  Wed", "星期四  Thu", "星期五  Fri", "星期六  Sat", "星期日  Sun"]
    return week[t.weekday()]  # t.weekday() 周一为0，周二为1...可作为列表的index
 
 
# 显示日期
def show_data(t):
    y = t.year
    m = t.month
    d = t.day
    return "{} 年 {} 月 {} 日".format(y, m, d)
 
 
# 显示时间
# def show_time(t):
#     m = t.minute
#     h = t.hour
#     return "{}:{}".format(h, m)
 
 
# 显示整个时钟
def show_clock():
    # 获取时间
    t = datetime.today()
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + second / 60.0
    hour = t.hour + minute / 60.0
 
    sec_hand.setheading(6 * second)
    min_hand.setheading(6 * minute)
    hou_hand.setheading(30 * hour)
 
    turtle.tracer(False)
 
    printer.forward(65)
    printer.write(show_week(t), align='center', font=("Courier", 14, "bold"))
 
    printer.back(65)
    printer.write("The Clock of Hua", align="center", font=("Courier", 16, "bold"))
 
    printer.back(65)
    printer.write(show_data(t), align='center', font=("Courier", 14, "bold"))
 
    # printer.back(25)
    # printer.write(show_time(t), align="center", font=("Courier", 14, "bold"))
    # 回到原点，以便于下一轮的显示
    printer.home()
    turtle.tracer(True)
 
    # 100ms后继续调用show_clock
    turtle.ontimer(show_clock, 100)
 
 
# main函数
def main():
    turtle.tracer(False)
    # 设置背景
    ts = turtle.getscreen()
    ts.bgcolor("#cccccc")
    # 初始化
    init_hand()
    # 设置时钟
    set_clock(180)
    turtle.tracer(True)
    # 显示时钟
    show_clock()
    turtle.mainloop()
 
 
if __name__ == "__main__":
    main()
