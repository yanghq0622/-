# -*- coding:utf-8 -*

import tkinter
from tkinter import ttk
import shelve
import datetime

# v0.1
# abceedfg

"""
testdata = {"张三":[["2017-01-22","1","2",""],["2018-02-11",'1','0',""]],
            "李四":[["2018-04-12",'1','0',""],["2018-05-17",'1','0',""],["2018-12-02",'0','2',""]],
            "王五":[["2017-01-22",'1','1',""],["2018-02-11",'1','0',""],["2019-01-12",'0','1',""]]
            }
"""

#读取文件
with shelve.open("./data/database") as data:
    user_data = data["user_data"]


class Mainframe(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__()
        self.title_name = tkinter.StringVar()   #标题变量
        self.title_name.set('工作服简易管理系统')
        self.button_info = tkinter.StringVar()  #底栏变量
        self.button_info.set("v0.1.2.4")
        self.config(bg = 'lightgrey')  #窗口背景
        self.long_num = tkinter.IntVar()  #
        self.short_num = tkinter.IntVar()
        self.long_date = ''
        self.short_date = ''
        
        self.adddate = tkinter.StringVar()
        #self.adddate.set(datetime.date.today())
        self.addlong = tkinter.IntVar()
        self.addshort = tkinter.IntVar()
        
        self.grid()
        self.draw_ui()  #绘制界面
        self.list_tree.bind('<ButtonRelease-1>', self.treeview_click)  #列表点击事件
        
    def draw_ui(self):

        #控件样式参数
        style = ttk.Style()
        style.configure("btn.TButton", font = ("微软雅黑", 16), foreground = '#333333')
        style.configure("fm.TFrame", background = '#1752BF')
        style.configure("TFrame",background = 'lightgrey')
        style.configure("lb.TLabel", foreground = 'white', background = '#1752BF', font = ("微软雅黑", 10, 'bold'))
        style.configure("TLabel", foreground = 'black', background = 'lightgrey')
        style.configure("TLabelFrame", padding = 10)
        ttk.Style().configure('Treeview', foreground= '#585F67')
        style.configure("Treeview.Heading", foreground= '#0D48AF',font = ("微软雅黑",10,"bold"))

        #标题
        ttk.Label(self, textvariable = self.title_name,font = ("微软雅黑",42,"bold")).grid(row = 3, column= 1, columnspan = 4, sticky = 'nsew', padx = 15, pady = 10,ipady = 10)
        
        #输入区
        self.fm = ttk.Frame(self, style = 'fm.TFrame')
        self.fm.grid(row = 3, column = 0, rowspan = 8, sticky = 'nsew',padx = 10,pady = 10)
                
        self.name_lb = ttk.Label(self.fm, text = "姓名:", style = 'lb.TLabel')
        self.name_lb.grid(row = 4, column = 0, sticky="w", padx = 10, pady = 4)
        self.select_name_cmd = (self.register(self.select_name),'%P') #姓名框 自动搜索函数 初始化
        self.name_entry = tkinter.Entry(self.fm, highlightcolor = 'dodgerblue', highlightthickness = 1, font = ("微软雅黑",18), validate = 'focusout', validatecommand = self.select_name_cmd, width = 10)
        self.name_entry.grid(row = 5, column = 0, sticky="nsew", padx = 10)
        
        self.date_lb = ttk.Label(self.fm, text = "日期:", style = 'lb.TLabel')
        self.date_lb.grid(row = 6, column = 0, sticky="w", padx = 10, pady = 4)
        #self.date_today_cmd = self.register(self.date_today)
        #self.prt_cmd = self.register(self.prt)
        #self.date_entry = tkinter.Entry(self.fm, highlightcolor = 'dodgerblue', highlightthickness = 1, font = ("微软雅黑",18),  validate = 'focusin', validatecommand = self.date_today_cmd, width = 10)
        self.x = tkinter.StringVar()
        
        #self.date_entry = tkinter.Entry(self.fm, highlightcolor = 'dodgerblue', highlightthickness = 1, font = ("微软雅黑",18),  textvariable = self.x, validate = 'focusout', validatecommand = self.date_today, invalidcommand = self.prt, width = 10)

        self.date_entry = tkinter.Entry(self.fm, highlightcolor = 'dodgerblue', highlightthickness = 1, font = ("微软雅黑",18), validate = 'focusout', validatecommand = self.date_today, invalidcommand = self.prt, width = 10)
        self.date_entry.grid(row = 7, column = 0, sticky="nsew", padx = 10)
        
        self.long_lb = ttk.Label(self.fm, text = "长袖:", style = 'lb.TLabel')
        self.long_lb.grid(row = 8, column = 0, sticky="nw", padx = 10, pady = 4)
        self.long_entry = tkinter.Spinbox(self.fm, highlightcolor = 'dodgerblue', highlightthickness = 1, from_ = 0, to = 10, font = ("微软雅黑",18), width = 10)
        self.long_entry.grid(row = 9, column = 0, sticky="nsew", padx = 10)
        
        self.short_lb = ttk.Label(self.fm, text = "短袖:", style = 'lb.TLabel')
        self.short_lb.grid(row = 10, column = 0, sticky="w", padx = 10, pady = 4)
        self.short_entry = tkinter.Spinbox(self.fm, highlightcolor = 'dodgerblue', highlightthickness = 1, from_ = 0, to = 10,font = ("微软雅黑",18), width = 10)
        self.short_entry.grid(row = 11, column = 0, sticky="nsew", padx = 10)

        self.notice_lb = ttk.Label(self.fm, text = "备注:", style = 'lb.TLabel')
        self.notice_lb.grid(row = 12, column = 0, sticky="w", padx = 10, pady = 4)
        self.notice_entry = tkinter.Entry(self.fm, highlightcolor = 'dodgerblue', highlightthickness = 1,font = ("微软雅黑",18), width = 10)
        self.notice_entry.grid(row = 13, column = 0, sticky="nsew", padx = 10, pady = 10)

        #按钮
        self.add_btn = ttk.Button(self.fm, text = "添加", style = "btn.TButton", command = self.add_recording)
        self.add_btn.grid(row = 14,column = 0, sticky = 'nsew', padx = 10, pady = 10)
        
        #tkinter.Label(self.fm, background = '#1752BF', height = 11).grid(row = 15, column = 0, sticky = 'nsew')
        
        self.del_btn = ttk.Button(self.fm, text = "删除", style = "btn.TButton", command = self.del_recording)
        self.del_btn.grid(row = 16, column = 0, sticky = 'nsew', padx = 10)

        #
        self.fm2 = ttk.Frame(self)
        self.fm2.grid(row = 4, column = 1, columnspan = 4, sticky = 'nsew', pady = 15, padx = 15)

        #可领取项目信息
        #self.info_lb1 = ttk.Label(self.fm2, text = "可领取： 长袖 {}  短袖 {}".format(self.long_num,self.short_num), font = ("微软雅黑",20))
        #self.info_lb1.grid(row = 4, column = 1, columnspan = 4, sticky = 'nsew',ipadx = 3,ipady = 3)
        #self.info_lb2 = ttk.Label(self.fm2, text = "下次领取时间： 长袖 {} 短袖 {}".format(self.long_date,self.short_date), font = ("微软雅黑",20))
        #self.info_lb2.grid(row = 5, column = 1, columnspan = 4, sticky = 'nsew',ipadx = 3,ipady = 3)
        tkinter.Label(self.fm2, text = "可领取： 长袖：", font = ("微软雅黑",30), background = 'lightgrey').grid(row = 4, column = 1)
        tkinter.Label(self.fm2, textvariable = self.long_num, font = ("微软雅黑",40,'bold'), foreground = 'blue', background = 'lightgrey').grid(row = 4, column = 2)
        tkinter.Label(self.fm2, text = "  短袖:  ", font = ("微软雅黑",30), background = 'lightgrey').grid(row = 4, column = 3)
        tkinter.Label(self.fm2, textvariable = self.short_num, font = ("微软雅黑",40,'bold'), foreground = 'blue', background = 'lightgrey').grid(row = 4, column = 4)
        

        #领取记录表
        tkinter.Label(self, text = "领取记录:",font = ("微软雅黑",9,'bold'), foreground= '#0D48AF', background = 'lightgrey').grid(row = 6, column = 1, sticky = 'sw', padx = 15)
        self.fm3 = ttk.Frame(self)
        self.fm3.grid(row = 7, column = 1, columnspan = 3, padx = 15, sticky = 'nw')

        self.list_tree = ttk.Treeview(self.fm3, column = [1, 2, 3, 4], show = 'tree headings', height = 15)
        self.list_tree.column('0',  anchor='center',width = 90)
        self.list_tree.column('1',  anchor='center',width = 150)
        self.list_tree.column('2',  anchor='center',width = 90)
        self.list_tree.column('3',  anchor='center',width = 90)
        self.list_tree.column('4',  anchor='center',width = 250)
        self.list_tree.heading('0', text='姓名')
        self.list_tree.heading('1', text='日期')
        self.list_tree.heading('2', text='长袖')
        self.list_tree.heading('3', text='短袖')
        self.list_tree.heading('4', text='备注')
        self.process_dict(user_data, self.list_tree, "") #遍历数据字典,插入数据
        self.list_tree.grid(row = 7, column = 1, rowspan = 9, columnspan = 4, pady = 10)
        self.list_tree.tag_configure('abc', font='微软雅黑 12')

        #底栏
        tkinter.Label(self, textvariable = self.button_info,font = ("微软雅黑",9), background = 'lightgrey').grid(row = 17, column= 0, columnspan = 5, sticky = 'w')

    def date_today(self):
        """
        self.date_entry.delete(0, 'end')
        self.date_entry.insert(0, str(datetime.date.today()))        
        self.date_entry.select_range(0, 'end')
        return True
        """
        a = self.date_entry.get()
        try:
            datetime.datetime.strptime(a,"%Y-%m-%d")            
            return True
        except:
            return False

    def prt(self):
        tp = "日期格式错误！！"
        self.button_info.set(tp)
        return True

    def is_vaild_date(self, date):
        try:
            datetime.datetime.strptime(date,"%Y-%m-%d")
            return True
        except:
            return False

    def cal_nums(self, name):
        
        templist = sorted(user_data[name], reverse = True)  
        self.long_num.set(2)
        self.short_num.set(2)
        long = 0
        short = 0
        #计算可领取长袖
        for i in range(len(templist)):
            if int(templist[i][1]) == 0:
                continue
            a = datetime.datetime.now() - datetime.datetime.strptime(templist[i][0], '%Y-%m-%d')
            if int(a.days) < 1825:
                long += int(templist[i][1])
        self.long_num.set(self.long_num.get() - long)
        #计算可领取短袖
        for i in range(len(templist)):
            if int(templist[i][2]) == 0:
                continue
            a = datetime.datetime.now() - datetime.datetime.strptime(templist[i][0], '%Y-%m-%d')
            if int(a.days) < 1825:
                short += int(templist[i][2])
        self.short_num.set(self.short_num.get() - short)

    def select_name(self, P):
        #自动输入当前日期 --->日期框
        t = datetime.date.today()
        self.date_entry.delete(0,'end')
        self.date_entry.insert(0,t)
        #
        if P != "" and P in user_data.keys():
            self.title_name.set(P)            #设置姓名 ---> 标题
            self.cal_nums(P)

        elif P == "":
            self.title_name.set('医生工作服简易管理系统')

        #     从treeview中选择      
        for i in range(len(self.list_tree.get_children(""))):
            if (self.list_tree.item(self.list_tree.get_children("")[i],'text')) == P:
                self.list_tree.selection_set(self.list_tree.get_children("")[i])
                self.list_tree.see(self.list_tree.get_children("")[i])
        return True

    def add_recording(self):
        #获取输入
        self.addname = self.name_entry.get()
        self.adddate = self.date_entry.get()
        self.addlong = self.long_entry.get()
        self.addshort = self.short_entry.get()
        self.addnotice = self.notice_entry.get()
        #self.name_entry.delete(0,'end')
        self.name_entry.focus_set()
        self.name_entry.selection_range(0,"end")
        self.notice_entry.delete(0,'end')

        #写入字典
        if self.addname == "":
            tp = "请输入姓名"
        elif self.addname in user_data.keys():
            record_list = user_data[(self.addname)]
            if self.is_vaild_date(self.date_entry.get()):
                if int(self.addlong) + int(self.addshort) != 0:
                    record_list.append([self.adddate, self.addlong, self.addshort,self.addnotice])
                    tp = "已增加记录：" + self.addname + " <--- " + self.adddate + " 长袖：" + self.addlong+ " 短袖： "+ self.addshort+ " "+self.addnotice
                else:
                    tp = "请输入工作服件数"
            else:
                tp = "日期格式不正确"
        else:
            if self.is_vaild_date(self.date_entry.get()):
                if int(self.addlong) + int(self.addshort) != 0:
                    user_data[self.addname] = [[self.adddate, self.addlong, self.addshort,self.addnotice]]
                    tp = "已增加记录：" + self.addname + " ---> " + self.adddate + " 长袖：" + self.addlong+ " 短袖： "+ self.addshort+ " "+self.addnotice
                else:
                    tp = "请输入工作服件数"
            else:
                tp = "日期格式不正确"

        #写入文件
        with shelve.open("./data/database") as data:
            data["user_data"] = user_data

        #刷新list_tree
        items = self.list_tree.get_children()
        [self.list_tree.delete(item) for item in items]
        self.process_dict(user_data, self.list_tree, "")

        self.button_info.set(tp)
        

    def del_recording(self):
        for item in self.list_tree.selection():            
            name_item = self.list_tree.item(self.list_tree.parent(item),'text')
            value_item = self.list_tree.item(item, 'values')            
            del_rec_list = user_data[name_item]
            del_rec_list.remove(list(value_item))
            tp = "已删除记录：" +name_item +" ---> "+ str(value_item)
            self.button_info.set(tp)
            if user_data[name_item] == []:
                del user_data[name_item]

        #刷新list_tree
        items = self.list_tree.get_children()
        [self.list_tree.delete(item) for item in items]
        self.process_dict(user_data, self.list_tree, "")

        #写入文件
        with shelve.open("./data/database") as data:
            data["user_data"] = user_data

    def treeview_click(self, v):
        for item in self.list_tree.selection():
            text = self.list_tree.item(item,'text')
            if text == "":
                text = self.list_tree.item(self.list_tree.parent(item),'text')
            values = self.list_tree.item(item, 'values')
            self.title_name.set(text)            
            self.cal_nums(text)


    def process_dict(self, d, tree, tr):
        for k, v in d.items():
            trr = tree.insert(tr, 'end', text = k, open = True, tag = 'abc' )
            for i in range(len(v)):
                tree.insert(trr, 'end', value = v[i], tag = 'abc')
"""
        for k,v in d.items():
            if type(v) == list:
                if type(v[0]) == dict:
                    trr = tree.insert(tr, 'end', text=k, open=True)
                    for ls in v:
                        self.process_dict(ls, tree, trr)
                else:
                    tree.insert(tr, 'end', text=k, values= v)
            elif type(v) == dict:
                trr = tree.insert(tr, 'end', text=k, open = Treu)
                self.process_dict(v, tree, trr)
  """    

if __name__ == "__main__":
    root = tkinter.Tk()
    root.columnconfigure(0,weight=1)
    root.rowconfigure(0,weight=1)
    root.title('医生工作服简易管理系统')
    Mainframe(root)
    root.mainloop()
        
