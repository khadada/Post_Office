BG_C = "#34495e"
title_font=('Dubai',42,'bold')
subtitle_font=('Dubai',20,'normal')
title_font_color="#fff"
primary_color = "#f1c40f"
success_color = "#27ae60"
favorit_c = "#ba52de"
btn_font = ('Dubai',14,'normal')
texts_list = ["أجمل صديقة","بسمة الحياة","أحلى من السكر","درة تماسين","من يسعد بلقائك"]
start_wiget = None
amount_window = None
# -----------------------------------------------------------------------
#------------------------------  Functionalty ---------------------------
# -----------------------------------------------------------------------
from tkinter import *
from tkinter import messagebox as letter
import random
def starting():
    start_wiget = Tk()
    start_wiget.title('ترحيب بــ: الأنسة التجاني خديجة')
    start_wiget.config(padx=100,pady=100)
    hello = Label(start_wiget,text=f'مرحبا بك يا {random.choice(texts_list)}',font=title_font)
    hello.grid(row=0,column=0,columnspan=2)

    start_btn = Button(start_wiget,text='بداية العمل',width=22,pady=30,bg=favorit_c,font=btn_font,command=ask_for_addition_amount)
    start_btn.grid(row=1,column=0)
    close_btn = Button(start_wiget,text=' عرض المعلومات',width=22,pady=30,bg=primary_color,font=btn_font)
    close_btn.grid(row=1,column=1)
    
    start_wiget.mainloop()
    
    
def get_amount():
    amount_window = Tk()
    amount_window.config(bg =BG_C,pady=100,padx=100)
    amount_window.title('إدخال المبلغ الذي سلم من المدير')
    title = Label(amount_window,text=' كم إستلمت من المدير يا خديجة',bg=BG_C,fg=title_font_color,font=title_font)
    title.grid(row=0,column=1,columnspan=2)
    lb = Label(amount_window,text='المبلغ',bg=BG_C,fg=title_font_color,font=subtitle_font)
    lb.grid(row=1,column=3,pady=50,padx=30)
    money = Entry(amount_window,borderwidth=20,relief=FLAT,font=title_font)
    money.focus()
    money.grid(row=1,column=1,columnspan=2,pady=50,padx=30)
    lb = Label(amount_window,text='دج',bg=BG_C,fg=title_font_color,font=subtitle_font)
    lb.grid(row=1,column=0,pady=50,padx=30)
    def done():
        global total_starting_amount
        total_starting_amount = int(money.get())
        amount_window.destroy()
    confirm_btn = Button(amount_window,text='واصل',width=28,pady=30,bg=success_color,font=btn_font,state=DISABLED,command=done)
    confirm_btn.grid(row=2,column=1)
    def confirm_amount():
        if len(money.get())>0:
            message_confirm = letter.askquestion('تأكيد المبلغ',message=f'هل أنت متأكدة يا خديخة أن المبلغ الذي إستلمتيه هو: {money.get()} دج')
            if message_confirm == 'yes':
                confirm_btn.config(state=NORMAL)
        else:
            letter.showerror(title='خطأ في الملبغ',message='أدخلي المبلغ من فظلك')
    confirm_continue = Button(amount_window,text='تأكيد',width=28,pady=30,bg=primary_color,font=btn_font,command=confirm_amount)
    confirm_continue.grid(row=2,column=2)
    amount_window.mainloop()

# -----------------------------------------------------------------------
#------------------------------  Setup UI -------------------------------
# -----------------------------------------------------------------------
def ask_for_addition_amount():
    message = letter.askyesno(title='عمل', message='يا خديجة هل إستلمت ملبغ جديد من المدير؟')
    if message:
        get_amount()
        
    
    else:
        letter.showinfo(title='للعلم فقط', message='ستواصلين العمل على المبلغ المتبقي الذي إستلمته المرة الأخيرة')
        return False

