# -*- encoding:utf-8 -*-

import time, datetime
import math
import itertools
import tkinter
import threading

import tkinter,sys,time
root=tkinter.Tk()
root.minsize(500, 500)
Label0=tkinter.Label(text=time.strftime('%Y-%m-%d',time.localtime(time.time())))
Label0.pack()
Label1=tkinter.Label(text=time.strftime('%H:%M:%S',time.localtime(time.time())))
Label1.pack()
year =time.strftime('%Y',time.localtime(time.time()))
year =int(year)
month =time.strftime('%m',time.localtime(time.time()))
month =int(month)
def tiangan(n):
    ge = int(n % 10)
    # print('ge',ge)
    tt = ge - 3
    # print(tt)
    if 6 >= tt >= 1:
        if tt == 1:
            tiangan = '甲'
        elif tt == 2:
            tiangan = '乙'
        elif tt == 3:
            tiangan = '丙'
        elif tt == 4:
            tiangan = '丁'
        elif tt == 5:
            tiangan = '戊'
        elif tt == 6:
            tiangan = '己'

    else:
        tt += 10
        if tt == 7:
            tiangan = '庚'
        elif tt == 8:
            tiangan = '辛'
        elif tt == 9:
            tiangan = '壬'
        elif tt == 10:
            tiangan = '癸'
    return tiangan

def dizhi(n):
    di = n % 12
    di += 9
    # print(di,'di')
    if 12 >= di >= 9:
        if di == 9:
            dizhi = '申'
            shuxiang = '候'
        elif di == 10:
            dizhi = '酉'
            shuxiang = '鸡'
        elif di == 11:
            dizhi = '戌'
            shuxiang = '狗'
        elif di == 12:
            dizhi = '亥'
            shuxiang = '猪'
    else:
        di -= 12
        if di == 1:
            dizhi = '子'
            shuxiang = '鼠'
        elif di == 2:
            dizhi = '丑'
            shuxiang = '牛'
        elif di == 3:
            dizhi = '寅'
            shuxiang = '虎'
        elif di == 4:
            dizhi = '卯'
            shuxiang = '兔'
        elif di == 5:
            dizhi = '辰'
            shuxiang = '龙'
        elif di == 6:
            dizhi = '巳'
            shuxiang = '蛇'
        elif di == 7:
            dizhi = '戊'
            shuxiang = '马'
        elif di == 8:
            dizhi = '未'
            shuxiang = '羊'
    return dizhi, shuxiang

def monthcheck():
    global yue
    mo = month
    o = tiangan(n)
    if o == '甲' or o == '己':
        if mo == 1:
            yue = '丙寅'
        elif mo == 2:
            yue = '丁卯'
        elif mo == 3:
            yue = '戊辰'
        elif mo == 4:
            yue = '己巳'
        elif mo == 5:
            yue = '庚午'
        elif mo == 6:
            yue = '辛未'
        elif mo == 7:
            yue = '壬申'
        elif mo == 8:
            yue = '癸酉'
        elif mo == 9:
            yue = '甲戌'
        elif mo == 10:
            yue = '乙亥'
        elif mo == 11:
            yue = '丙子'
        elif mo == 12:
            yue = '丁丑'
    elif o == '乙' or o == '庚':
        if mo == 1:
            yue = '戊寅'
        elif mo == 2:
            yue = '己卯'
        elif mo == 3:
            yue = '庚辰'
        elif mo == 4:
            yue = '辛巳'
        elif mo == 5:
            yue = '壬午'
        elif mo == 6:
            yue = '癸未'
        elif mo == 7:
            yue = '甲申'
        elif mo == 8:
            yue = '乙酉'
        elif mo == 9:
            yue = '丙戌'
        elif mo == 10:
            yue = '丁亥'
        elif mo == 11:
            yue = '戊子'
        elif mo == 12:
            yue = '己丑'
    elif o == '丙' or o == '辛':
        if mo == 1:
            yue = '庚寅'
        elif mo == 2:
            yue = '辛卯'
        elif mo == 3:
            yue = '壬辰'
        elif mo == 4:
            yue = '癸巳'
        elif mo == 5:
            yue = '甲午'
        elif mo == 6:
            yue = '乙未'
        elif mo == 7:
            yue = '丙申'
        elif mo == 8:
            yue = '丁酉'
        elif mo == 9:
            yue = '戊戌'
        elif mo == 10:
            yue = '己亥'
        elif mo == 11:
            yue = '庚子'
        elif mo == 12:
            yue = '辛丑'
    elif o == '丁' or o == '壬':
        if mo == 1:
            yue = '壬寅'
        elif mo == 2:
            yue = '癸卯'
        elif mo == 3:
            yue = '甲辰'
        elif mo == 4:
            yue = '乙巳'
        elif mo == 5:
            yue = '丙午'
        elif mo == 6:
            yue = '丁未'
        elif mo == 7:
            yue = '戊申'
        elif mo == 8:
            yue = '己酉'
        elif mo == 9:
            yue = '庚戌'
        elif mo == 10:
            yue = '辛亥'
        elif mo == 11:
            yue = '壬子'
        elif mo == 12:
            yue = '癸丑'
    elif o == '戊' or o == '癸':
        if mo == 1:
            yue = '甲寅'
        elif mo == 2:
            yue = '乙卯'
        elif mo == 3:
            yue = '丙辰'
        elif mo == 4:
            yue = '丁巳'
        elif mo == 5:
            yue = '戊午'
        elif mo == 6:
            yue = '己未'
        elif mo == 7:
            yue = '庚申'
        elif mo == 8:
            yue = '辛酉'
        elif mo == 9:
            yue = '壬戌'
        elif mo == 10:
            yue = '癸亥'
        elif mo == 11:
            yue = '甲子'
        elif mo == 12:
            yue = '乙丑'
    return yue
if (year % 4 == 0) & (year % 100 != 0):
    yeartext = "今年是闰年"
elif year % 400 == 0:
    yeartext = "今年不是闰年"
else:
    yeartext = "今年是闰年"
n = year
a = tiangan(n)
l, z = dizhi(n)
b = monthcheck()
tiangandizhi='%s%s%s%s%s%s'%(a,l,z,'年',b,'月')
Label2=tkinter.Label(text=tiangandizhi)
Label2.pack()
Label2=tkinter.Label(text=yeartext)
Label2.pack()

def trickit():
    currentTime=time.strftime('%H:%M:%S',time.localtime(time.time()))
    Label1.config(text=currentTime)
    root.update()
    Label1.after(1000, trickit)
Label1.after(1000, trickit)

def get_clock_step(base_pntr, long_pntr):
    pos = []
    for i in range(60):
        pos.append((base_pntr[0] + long_pntr * math.cos(i * math.pi / 30),
                    base_pntr[0] + long_pntr * math.sin(i * math.pi / 30)))
    return pos[45:] + pos[:45]


def gen_i_pos(c_pntr, long_pntr):
    for i, p in enumerate(get_clock_step(c_pntr, long_pntr)):
        yield i, p


class Pointer:

    def __init__(self, c_pntr, long_pntr, cvns, scale=None, super_pntr=None, width=1, fill='black'):
        # 参数说明：
        # c_pntr: 表盘的中心坐标；
        # long_pntr: 表针长；
        # cvns: 画布引用；
        # scale: 指针行走比例；
        # super_pntr: 上级指针；
        # width: 指针粗细；
        # fill: 指针颜色；
        self.pos_iter = itertools.cycle(gen_i_pos(c_pntr, long_pntr))
        self.scale = scale
        self.cvns = cvns
        self.crrnt_pos = self.pos_iter.__next__()[1]
        self.c_pntr = c_pntr
        self.super_pntr = super_pntr
        self.id_pntr = None
        self.width = width
        self.fill = fill

    def draw(self):
        self.id_pntr = cvns.create_line(self.c_pntr, self.crrnt_pos, width=self.width, fill=self.fill)

    def walk_step(self):
        self.delete()
        self.draw()
        i, self.crrnt_pos = self.pos_iter.__next__()
        if self.super_pntr and self.scale and (i + 1) % self.scale == 0:
            self.super_pntr.walk_step()

    def delete(self):
        if self.id_pntr:
            self.cvns.delete(self.id_pntr)

    def set_start(self, steps):
        for i in range(steps - 1):
            self.pos_iter.__next__()
        self.crrnt_pos = self.pos_iter.__next__()[1]


class PlateImg:

    def __init__(self, c_pntr, clock_r, cvns, img):
        self.cvns = cvns
        self.clock_r = clock_r
        self.c_pntr = c_pntr
        self.img = img
        self.pid = None
        self.draw()

    def draw(self):
        self.im = tkinter.PhotoImage(file=self.img)
        self.pid = self.cvns.create_image(self.c_pntr, image=self.im)

    def delete(self):
        if self.pid:
            self.cvns.delete(self.pid)

    def set_img(self, img):
        self.img = img
        self.delete()
        self.draw()


class InImg(PlateImg):
    def draw(self):
        x = self.c_pntr[0]
        y = self.c_pntr[0] + self.clock_r / 5
        self.im = tkinter.PhotoImage(file=self.img)
        self.pid = self.cvns.create_image(x, y, image=self.im)


class CustomPlate:
    def __init__(self, c_pntr, clock_r, cvns, imgp='platex.gif', imgi='flowersx.gif'):
        self.pi = PlateImg(c_pntr, clock_r, cvns, imgp)
        self.ii = InImg(c_pntr, clock_r, cvns, imgi)

    def set_img(self, imgp, imgi):
        self.pi.set_img(imgp)
        self.ii.set_img(imgi)

    def delete(self):
        self.pi.delete()
        self.ii.delete()


class Plate:

    def __init__(self, c_pntr, clock_r, cvns, long=10):
        self.pos_a = get_clock_step(c_pntr, clock_r - long)
        self.pos_b = get_clock_step(c_pntr, clock_r)
        self.cvns = cvns
        self.plates = []
        self.draw()

    def draw(self):
        for i, p in enumerate(zip(self.pos_a, self.pos_b)):
            width = 5 if (i + 1) % 5 == 0 else 3
            pid = self.cvns.create_line(*p, width=width)
            self.plates.append(pid)

    def delete(self):
        if self.plates:
            for item in self.plates:
                self.cvns.delete(item)


class MyClock:

    def __init__(self, base_pntr, clock_r, cvns):
        self.c_pntr = base_pntr
        self.clock_r = clock_r
        self.cvns = cvns
        self.plate = Plate(base_pntr, clock_r, self.cvns)
        h, m, s = self.start_time()
        self.h_pntr = Pointer(base_pntr, 3 * clock_r // 5, self.cvns, width=5, fill='blue')
        self.m_pntr = Pointer(base_pntr, 4 * clock_r // 5, self.cvns, 12, super_pntr=self.h_pntr, width=3, fill='green')
        self.h_pntr.set_start(h * 5)
        self.m_pntr.set_start(m)
        self.h_pntr.walk_step()
        self.m_pntr.walk_step()
        self.s_pntr = Pointer(base_pntr, clock_r - 5, self.cvns, 60, super_pntr=self.m_pntr, fill='red')
        self.s_pntr.set_start(s)

    def chg_plate(self):
        self.plate.delete()
        if isinstance(self.plate, CustomPlate):
            self.plate = Plate(self.c_pntr, self.clock_r, self.cvns)
        else:
            self.plate = CustomPlate(self.c_pntr, self.clock_r, self.cvns)
        self.h_pntr.delete()
        self.h_pntr.draw()
        self.m_pntr.delete()
        self.m_pntr.draw()

    def set_img(self, imgp, imgi):
        if not isinstance(self.plate, CustomPlate):
            self.chg_plate()
        self.plate.set_img(imgp, imgi)

    def walk_step(self):
        self.s_pntr.walk_step()

    def start_time(self):
        crrnt_time = datetime.datetime.now()
        hour = crrnt_time.hour
        minute = crrnt_time.minute
        second = crrnt_time.second
        return hour, minute, second


class MyButton:
    def __init__(self, root, clock):
        self.clock = clock
        button = tkinter.Button(root, text='', command=self.chg_plate)

    def chg_plate(self):
        self.clock.chg_plate()


class MyTk(tkinter.Tk):
    def quit(self):
        StartClock.looping = False
        self.quit()


class StartClock:
    looping = True

    def __init__(self, mc, root):
        self.mc = mc
        self.root = root

    def start_clock(self):
        while StartClock.looping:
            self.mc.walk_step()
            self.root.update()
            time.sleep(0.05)


if __name__ == '__main__':
    root = MyTk()
    cvns = tkinter.Canvas(root, width=400, height=400, bg='white')
    cvns.pack()
    mc = MyClock((200, 200), 200, cvns)
    bt = MyButton(root, mc)
    t = threading.Thread(target=StartClock(mc, root).start_clock)
    t.setDaemon(True)
    t.start()
    root.resizable(False, False)
    root.mainloop()
