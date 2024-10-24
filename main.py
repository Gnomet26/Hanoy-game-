import tkinter as tk
import tkinter.messagebox as messagebox
import time
from threading import Thread

class MyGame:

    def __init__(self):

        #============================ O'zgaruvchilar ================================

        self.nishonda = None
        self.nishonda_index = None

        self.is_touch = True
        self.winner = False
        self.timer_index = 0
        self.ustun_1_massiv = []
        self.ustun_2_massiv = []
        self.ustun_3_massiv = []

        #============================================================================

        #=========================== Tkinter window =================================

        self.oyna = tk.Tk()
        self.oyna.geometry("1100x550")
        self.oyna.resizable(False, False)
        self.oyna.title("Hanoy minorasi")
        self.oyna.bind("<Destroy>", lambda x: self.close_window())
        #============================================================================

        #======================== Canvas window =======================================

        self.my_canvas = tk.Canvas(master=self.oyna,width=1000,height=400,bg="#9ffffc")
        self.my_canvas.place(x = 50,y = 70)

        #===============================================================================


        #=============================== Game widgets ==================================

        self.usttun_1 = self.my_canvas.create_rectangle(145,150,165,400,fill="#ffca15")
        self.usttun_2 = self.my_canvas.create_rectangle(480, 150, 500, 400, fill="#ffca15")
        self.usttun_3 = self.my_canvas.create_rectangle(820, 150, 840, 400, fill="#ffca15")

        #===============================================================================


        #============================== Bo'laklar ======================================

        self.bolak_1 = self.my_canvas.create_rectangle(40,370,270,400,fill="red")
        self.bolak_2 = self.my_canvas.create_rectangle(60, 340, 250, 370, fill="#ff8615")
        self.bolak_3 = self.my_canvas.create_rectangle(80, 310, 230, 340, fill="#fffb15")
        self.bolak_4 = self.my_canvas.create_rectangle(100, 280, 210, 310, fill="#51ff15")
        self.bolak_5 = self.my_canvas.create_rectangle(120, 250, 190, 280, fill="#15ffb1")
        self.bolak_6 = self.my_canvas.create_rectangle(140, 220, 170, 250, fill="#153cff")

        self.ustun_1_massiv.insert(0,self.bolak_1)
        self.ustun_1_massiv.insert(0, self.bolak_2)
        self.ustun_1_massiv.insert(0, self.bolak_3)
        self.ustun_1_massiv.insert(0, self.bolak_4)
        self.ustun_1_massiv.insert(0, self.bolak_5)
        self.ustun_1_massiv.insert(0, self.bolak_6)

        #===============================================================================


        #=================================== Buttons ===================================

        self.button_1 = tk.Button(master=self.oyna,text="Button1",font=("Arial",16),command= lambda :self.runn_th_1())
        self.button_1.place(x = 150,y = 15)

        self.button_2 = tk.Button(master=self.oyna, text="Button2", font=("Arial", 16),command= lambda :self.runn_th_2())
        self.button_2.place(x=490, y=15)

        self.button_3 = tk.Button(master=self.oyna, text="Button3", font=("Arial", 16),command= lambda :self.runn_th_3())
        self.button_3.place(x=830, y=15)

        #=================================================================================

        #================================= timer widget ==================================

        self.timer_l = tk.Label(self.oyna,font=("Arial",20,"bold"),text="Timer  0:0:0")
        self.timer_l.place(x = 50,y = 500)

        th = Thread(target=lambda: self.timer_label())
        th.start()
        #=================================================================================

        #======================= Window looping ==========================================

        self.oyna.bind("<Destroy>", lambda x:self.close_window())
        self.oyna.update()
        self.oyna.mainloop()

        #=================================================================================

    def close_window(self):
        self.winner = True

    def move_item(self,item,dx,dy,type):
        if type == "top":
            if self.my_canvas.coords(item)[1] >= dy and self.my_canvas.coords(item)[0] == dx:
                self.my_canvas.move(item,0,-3)
                time.sleep(0.001)
                self.move_item(item,dx,dy,type)
            else:
                self.is_touch = True
        elif type == "right":
            if self.my_canvas.coords(item)[1] == dy and self.my_canvas.coords(item)[0] <= dx:
                self.my_canvas.move(item,3,0)
                time.sleep(0.001)
                self.move_item(item,dx,dy,type)
            else:
                self.is_touch = True
        elif type == "bottom":
            if self.my_canvas.coords(item)[1] <= dy and self.my_canvas.coords(item)[0] == dx:
                self.my_canvas.move(item,0,3)
                time.sleep(0.001)
                self.move_item(item,dx,dy,type)
            else:
                self.is_touch = True
        elif type == "left":
            if self.my_canvas.coords(item)[1] == dy and self.my_canvas.coords(item)[0] >= dx:
                self.my_canvas.move(item,-3,0)
                time.sleep(0.001)
                self.move_item(item,dx,dy,type)
            else:
                self.is_touch = True
    def runn_1(self):
        if self.is_touch:
            if self.nishonda == None:
                if len(self.ustun_1_massiv) > 0:
                    self.is_touch = False
                    self.nishonda = self.ustun_1_massiv[0]
                    self.nishonda_index = 1
                    th = Thread(target=lambda :self.move_item(self.nishonda,self.my_canvas.coords(self.nishonda)[0],49,"top"))
                    th.start()
            else:
                if self.nishonda_index == 1:
                    self.is_touch = False
                    th = Thread(target=lambda: self.move_item(self.nishonda,self.my_canvas.coords(self.nishonda)[0],369 - (len(self.ustun_1_massiv)-1)*30,"bottom"))
                    th.start()
                    self.nishonda = None
                    self.nishonda_index = None
                elif self.nishonda_index == 2:
                    if len(self.ustun_1_massiv) == 0 or self.ustun_1_massiv[0] < self.nishonda:
                        self.is_touch = False
                        self.ustun_2_massiv.remove(self.nishonda)
                        self.ustun_1_massiv.insert(0, self.nishonda)
                        if self.nishonda == self.bolak_1:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 41, self.my_canvas.coords(self.nishonda)[1],
                                                              "left"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_2:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 61, self.my_canvas.coords(self.nishonda)[1],
                                                              "left"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_3:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 81, self.my_canvas.coords(self.nishonda)[1],
                                                              "left"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_4:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 101, self.my_canvas.coords(self.nishonda)[1],
                                                              "left"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_5:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 121, self.my_canvas.coords(self.nishonda)[1],
                                                              "left"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_6:

                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 141, self.my_canvas.coords(self.nishonda)[1],
                                                              "left"))
                            th.start()
                            pass
                        self.is_touch = False
                        time.sleep(0.5)
                        self.is_touch = False
                        th2 = Thread(target=lambda: self.move_item(self.nishonda, self.my_canvas.coords(self.nishonda)[0],369 - (len(self.ustun_1_massiv) - 1) * 30, "bottom"))
                        th2.start()
                        self.nishonda = None
                        self.nishonda_index = None
                        pass
                elif self.nishonda_index == 3:
                    if len(self.ustun_1_massiv) == 0 or self.ustun_1_massiv[0] < self.nishonda:
                        self.is_touch = False
                        self.ustun_3_massiv.remove(self.nishonda)
                        self.ustun_1_massiv.insert(0, self.nishonda)
                        if self.nishonda == self.bolak_1:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 41, self.my_canvas.coords(self.nishonda)[1],
                                                              "left"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_2:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 61, self.my_canvas.coords(self.nishonda)[1],
                                                              "left"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_3:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 81, self.my_canvas.coords(self.nishonda)[1],
                                                              "left"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_4:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 101, self.my_canvas.coords(self.nishonda)[1],
                                                              "left"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_5:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 121, self.my_canvas.coords(self.nishonda)[1],
                                                              "left"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_6:

                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 141, self.my_canvas.coords(self.nishonda)[1],
                                                              "left"))
                            th.start()
                            pass
                        self.is_touch = False
                        time.sleep(0.3)
                        self.is_touch = False
                        th2 = Thread(target=lambda: self.move_item(self.nishonda, self.my_canvas.coords(self.nishonda)[0],
                                                                   369 - (len(self.ustun_1_massiv) - 1) * 30, "bottom"))
                        th2.start()
                        self.nishonda = None
                        self.nishonda_index = None
                        pass
            pass
        pass
    def runn_2(self):
        if self.is_touch:
            if self.nishonda == None:
                if len(self.ustun_2_massiv) > 0:
                    self.is_touch = False
                    self.nishonda = self.ustun_2_massiv[0]
                    self.nishonda_index = 2
                    th = Thread(target=lambda: self.move_item(self.nishonda, self.my_canvas.coords(self.nishonda)[0], 49,"top"))
                    th.start()
            else:
                if self.nishonda_index == 1:
                    if len(self.ustun_2_massiv) == 0 or self.ustun_2_massiv[0] < self.nishonda:
                        self.is_touch = False
                        self.ustun_1_massiv.remove(self.nishonda)
                        self.ustun_2_massiv.insert(0,self.nishonda)
                        if self.nishonda == self.bolak_1:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 373, self.my_canvas.coords(self.nishonda)[1],
                                                              "right"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_2:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 393, self.my_canvas.coords(self.nishonda)[1],
                                                              "right"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_3:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 413, self.my_canvas.coords(self.nishonda)[1],
                                                              "right"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_4:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 433, self.my_canvas.coords(self.nishonda)[1],
                                                              "right"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_5:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 453, self.my_canvas.coords(self.nishonda)[1],
                                                              "right"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_6:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 473, self.my_canvas.coords(self.nishonda)[1],
                                                              "right"))
                            th.start()
                        pass
                        self.is_touch = False
                        time.sleep(0.5)
                        self.is_touch = False
                        th2 = Thread(target=lambda: self.move_item(self.nishonda, self.my_canvas.coords(self.nishonda)[0], 369 - (len(self.ustun_2_massiv) - 1) * 30, "bottom"))
                        th2.start()
                        self.nishonda = None
                        self.nishonda_index = None
                elif self.nishonda_index == 2:
                    self.is_touch = False
                    th = Thread(target=lambda: self.move_item(self.nishonda, self.my_canvas.coords(self.nishonda)[0],369 - (len(self.ustun_2_massiv) - 1) * 30, "bottom"))
                    th.start()
                    self.nishonda = None
                    self.nishonda_index = None
                elif self.nishonda_index == 3:
                    if len(self.ustun_2_massiv) == 0 or self.ustun_2_massiv[0] < self.nishonda:
                        self.is_touch = False
                        self.ustun_3_massiv.remove(self.nishonda)
                        self.ustun_2_massiv.insert(0, self.nishonda)
                        if self.nishonda == self.bolak_1:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 377, self.my_canvas.coords(self.nishonda)[1],
                                                              "left"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_2:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 397, self.my_canvas.coords(self.nishonda)[1],
                                                              "left"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_3:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 417, self.my_canvas.coords(self.nishonda)[1],
                                                              "left"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_4:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 437, self.my_canvas.coords(self.nishonda)[1],
                                                              "left"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_5:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 457, self.my_canvas.coords(self.nishonda)[1],
                                                              "left"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_6:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 477, self.my_canvas.coords(self.nishonda)[1],
                                                              "left"))
                            th.start()
                            pass
                        self.is_touch = False
                        time.sleep(0.5)
                        self.is_touch = False
                        th2 = Thread(target=lambda: self.move_item(self.nishonda, self.my_canvas.coords(self.nishonda)[0],
                                                                   369 - (len(self.ustun_2_massiv) - 1) * 30, "bottom"))
                        th2.start()
                        self.nishonda = None
                        self.nishonda_index = None

    def runn_3(self):
        if self.is_touch:
            if self.nishonda == None:
                if len(self.ustun_3_massiv) > 0:
                    self.is_touch = False
                    self.nishonda = self.ustun_3_massiv[0]
                    self.nishonda_index = 3
                    th = Thread(target=lambda: self.move_item(self.nishonda, self.my_canvas.coords(self.nishonda)[0], 49,"top"))
                    th.start()

            else:
                if self.nishonda_index == 1:
                    if len(self.ustun_3_massiv) == 0 or self.ustun_3_massiv[0] < self.nishonda:

                        self.is_touch = False
                        self.ustun_1_massiv.remove(self.nishonda)
                        self.ustun_3_massiv.insert(0,self.nishonda)
                        if self.nishonda == self.bolak_1:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 713, self.my_canvas.coords(self.nishonda)[1],
                                                              "right"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_2:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 733, self.my_canvas.coords(self.nishonda)[1],
                                                              "right"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_3:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 753, self.my_canvas.coords(self.nishonda)[1],
                                                              "right"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_4:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 773, self.my_canvas.coords(self.nishonda)[1],
                                                              "right"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_5:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 793, self.my_canvas.coords(self.nishonda)[1],
                                                              "right"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_6:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 813, self.my_canvas.coords(self.nishonda)[1],
                                                              "right"))
                            th.start()
                            pass
                        self.is_touch = False
                        time.sleep(0.5)
                        self.is_touch = False
                        th2 = Thread(target=lambda: self.move_item(self.nishonda, self.my_canvas.coords(self.nishonda)[0],369 - (len(self.ustun_3_massiv) - 1) * 30, "bottom"))
                        th2.start()
                        self.nishonda = None
                        self.nishonda_index = None
                        if len(self.ustun_3_massiv) == 6:
                            self.winner = True
                            messagebox.showinfo("tabriklaymiz!","Siz o'yinni yutdingiz : - )")
                elif self.nishonda_index == 2:
                    if len(self.ustun_3_massiv) == 0 or self.ustun_3_massiv[0] < self.nishonda:
                        self.is_touch = False
                        self.ustun_2_massiv.remove(self.nishonda)
                        self.ustun_3_massiv.insert(0, self.nishonda)

                        if self.nishonda == self.bolak_1:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 713, self.my_canvas.coords(self.nishonda)[1],
                                                              "right"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_2:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 733, self.my_canvas.coords(self.nishonda)[1],
                                                              "right"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_3:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 753, self.my_canvas.coords(self.nishonda)[1],
                                                              "right"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_4:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 773, self.my_canvas.coords(self.nishonda)[1],
                                                              "right"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_5:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 793, self.my_canvas.coords(self.nishonda)[1],
                                                              "right"))
                            th.start()
                            pass
                        elif self.nishonda == self.bolak_6:
                            th = Thread(
                                target=lambda: self.move_item(self.nishonda, 813, self.my_canvas.coords(self.nishonda)[1],
                                                              "right"))
                            th.start()
                            pass
                        self.is_touch = False
                        time.sleep(0.5)
                        self.is_touch = False
                        th2 = Thread(target=lambda: self.move_item(self.nishonda, self.my_canvas.coords(self.nishonda)[0],
                                                                   369 - (len(self.ustun_3_massiv) - 1) * 30, "bottom"))
                        th2.start()
                        self.nishonda = None
                        self.nishonda_index = None
                        if len(self.ustun_3_massiv) == 6:
                            self.winner = True
                            messagebox.showinfo("tabriklaymiz!","Siz o'yinni yutdingiz : - )")
                elif self.nishonda_index == 3:
                    self.is_touch = False
                    th = Thread(target=lambda: self.move_item(self.nishonda, self.my_canvas.coords(self.nishonda)[0],
                                                              369 - (len(self.ustun_3_massiv) - 1) * 30, "bottom"))
                    th.start()
                    self.nishonda = None
                    self.nishonda_index = None

    def runn_th_1(self):

        th = Thread(target=lambda :self.runn_1())
        th.start()


    def runn_th_2(self):

        th = Thread(target=lambda : self.runn_2())
        th.start()

    def runn_th_3(self):

        th = Thread(target=lambda :self.runn_3())
        th.start()

    def timer_label(self):
        if not self.winner:
            ind = self.timer_index
            hours = ind / 3600
            ind %= 3600
            minut = ind / 60
            ind %= 60
            sekund = ind
            self.timer_l.config(text=f"Timer  {int(hours)}:{int(minut)}:{int(sekund)}")
            time.sleep(1)
            self.timer_index+=1
            self.timer_label()

if __name__ == "__main__":
    MyGame()