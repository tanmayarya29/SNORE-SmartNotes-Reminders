#<----------------notes n reminders -by tanmay---------------------->
import os
try:
    from tkinter import *
    from tkinter import ttk
    from tkinter.colorchooser import askcolor 
    from tkcalendar import Calendar, DateEntry
    from ttkthemes import *
    from tkinter.filedialog import askopenfile 
    from time import strftime,sleep 
    from datetime import datetime,date
    from PIL import ImageTk, Image
    from threading import Thread
    import pygame
    import speech_recognition as sr
except:
    os.system('pip install tk')
    os.system('pip install tkcalendar')
    os.system('pip install ttkthemes')
    os.system('pip install datetime')
    os.system('pip install pillow')
    os.system('pip install threaded')
    os.system('pip install python-vlc')
    os.system('pip install pipwin')
    os.system('pipwin install pyaudio')
    os.system('pip install speechrecognition')
finally:
    from tkinter import *
    from tkinter import ttk
    from tkinter.colorchooser import askcolor 
    from tkcalendar import Calendar, DateEntry
    from ttkthemes import *
    from tkinter.filedialog import askopenfile 
    from time import strftime,sleep 
    from datetime import datetime,date
    from PIL import ImageTk, Image
    from threading import Thread
    import pygame
    import speech_recognition as sr


#Functions
note={}
favNotes={}
seldate=[]
seltim=[]
count=0
def inp_note(title,content,colr):
    
    if content=='' and title=='':
        return 0
    title=title
    day=datetime.now()
    title=title+day.strftime('  ----->  %H:%M:%p  ')+day.strftime('%d/%m/%Y')
    content=content
    lstnts.configure(font = ('calibri', 10, 'bold'))
    lstnts.insert(0,title,content)
    # lf=LabelFrame(lstnts,text=title,bg=colr)
    # lf.pack(side=BOTTOM,fill=BOTH)
    # lbl=Label(lf,text=content,bg=colr)
    # lbl.pack(side=LEFT)

def fav_note(title,content,colr): 
    if content=='' and title=='':
        return 0
    title=title
    day=datetime.now()
    title=title+day.strftime(' %H:%M:%p  ')+day.strftime('%d/%m/%Y')
    content=content
    lf=LabelFrame(lblfrm3,text=title,bg=colr)
    lf.pack(side=BOTTOM,fill=BOTH)
    Label(lf,text=content).pack()

def remindr(title,content,colr,remdate,remtime): 
    title=title
    day=datetime.now()
    title=title+day.strftime(' %H:%M:%p  ')+day.strftime('%d/%m/%Y')
    content=content
    lf=LabelFrame(lblfrm2,text=title,bg=colr)
    lf.pack(side=BOTTOM,fill=BOTH)
    l1=Label(lf,text=content)
    l2=Label(lf,text=remdate)
    l3=Label(lf,text=remtime)
    l1.pack()
    l2.pack()
    l3.pack()
    #playAlarm
    def play_sound():
        file = 'rem.mp3'
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        sleep(8)
        pygame.mixer.music.play()



    #Less Values or Wrong differentiator chk
    try:
        dateS=remdate
        dateStr=dateS.split('-')
        dateStr.reverse()
        print(dateStr)
        timeS=remtime
        timeStr=timeS.split(':')
        timeStr[2]=timeStr[2].upper()
        print(dateS,timeS,dateStr,timeStr)
    except:
        print('Err:Less Values or Wrong differentiator used!/nTry again')
        quit()

    #time format chk
    def time_checker(timeStr):
        if (int(timeStr[0])<13 and int(timeStr[0])>0 and int(timeStr[1])<61 and int(timeStr[1])>=0 and (timeStr[2]=='AM' or timeStr[2]=='PM')):
            return True
        else:
            print("Err:Wrong time Entered")
            return False

    # Format chk
    try:
        tchk=time_checker(timeStr)
    except:
        print('Err:Format Error!/nTry Again')
        quit()

    #24hour time converter
    def army_time(tim):
        if tim[2] =='AM':
            if int(tim[0])==12:
                return 0,int(tim[1])
            else:
                return int(tim[0]),int(tim[1])
        else:
            if int(tim[0])==12:
                return 12,int(tim[1])
            else:
                return int(tim[0])+12,int(tim[1])
    if tchk :
        ch,cm=army_time(timeStr)
        print(ch,cm)
    else:
        quit()
    def plyalrm():
        while True:
            now=datetime.now()
            timeN = now.strftime("%H:%M")
            dateN = now.strftime("%D/%M/%Y")
            rem1=dateN.split('/')
            remD=int(dateStr[0])-int(rem1[1])
            remMnt=int(dateStr[1])-int(rem1[0])
            remY=int(dateStr[2])-int(rem1[4])
            rem=timeN.split(':')
            remH=-int(rem[0])+ch
            remM=-int(rem[1])+cm
            
            if (remY==0 and remMnt ==0 and remD==0 and remH==0 and remM==0) :
                Thread().start()
                tlrem=Toplevel()
                tlrem.iconbitmap('remndr.ico')
                tlrem.geometry('240x240')
                tlrem.title('REMINDER')
                phto=PhotoImage(file='school-bell.png')
                Label(tlrem,image=phto,bg=colr).pack(side=TOP,fill=BOTH,expand=TRUE)
                Label(tlrem,text='Title-> '+title,bg=colr).pack(side=TOP,fill=BOTH,expand=TRUE)
                Label(tlrem,text='Note-> '+content,bg=colr).pack(side=TOP,fill=BOTH,expand=TRUE)
                Button(tlrem,text='Quit',command=tlrem.destroy).pack(side=TOP,fill=BOTH,expand=TRUE)
                tlrem.wm_attributes("-topmost", 1)
                # root.wm_attributes("-topmost", 1)
                play_sound()
                tlrem.destroy()
                break
                
                
    Thread(target=plyalrm).start()
    seldate.clear()
    seltim.clear()

def ad_img(title,content,colr):
    def open_file(): 
        file = askopenfile(filetypes =[('Images', '*.png'),('Images','*.jpeg'),('Images','*.jpg')])
        file=str(file.name)
        # im=Image.open(file)
        # im.show()
        return file
    # imgjlst = Label(lstnts,height=20)
    # imgjlst.pack(side=TOP)
    def list_entry_clicked(*ignore):
        imgname = lstnts.get(lstnts.curselection())
        # imgname1=PhotoImage(file=imgname)
        # imgjlst.config(image=imgname1)
        Image.open(imgname).show()
    fil=open_file()
    # adimg=PhotoImage(file=fil)
    if fil=='':
        return 0
    title=title
    day=datetime.now()
    title=title+day.strftime('  ----->  %H:%M:%p  ')+day.strftime('%d/%m/%Y')
    content=content
    lstnts.configure(font = ('calibri', 10, 'bold'))
    lstnts.insert(0,title,'Click below to see your image...',fil,content)
    lstnts.bind('<ButtonRelease-1>', list_entry_clicked)
    # lf=LabelFrame(lstnts,text=title,bg=colr)
    # lf.pack(side=BOTTOM,fill=BOTH)
    # lbl=Label(lf,text=content,bg=colr)
    # lbl.pack(side=LEFT)
def dark_md():
    root.configure(theme='equilux')
    botton_frm.configure(bg='black')
    lblfrm1.configure(bg='black',fg='white')
    lblfrm12.configure(bg='black',fg='white')
    lstnts.configure(bg='black',fg='white')
    lblfrm2.configure(bg='black',fg='white')
    lblfrm3.configure(bg='black',fg='white')
def light_md():
    root.configure(theme='breeze')
    botton_frm.configure(bg='white')
    lblfrm1.configure(fg='black',bg='white')
    lblfrm12.configure(fg='black',bg='white')
    lstnts.configure(fg='black',bg='white')
    lblfrm2.configure(fg='black',bg='white')
    lblfrm3.configure(fg='black',bg='white')
def micon(a):
    def micbt():
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            b=''
            while a:
                try:
                    print('Speak...')
                    audio = recognizer.listen(source)
                    if b=='t':
                        print('Title:',end=' ')
                        print(str(recognizer.recognize_google(audio)))
                        titl.insert(END,str(recognizer.recognize_google(audio)))
                    # print (recognizer.recognize_sphinx(audio) )
                    
                    if str(recognizer.recognize_google(audio))=='done':#ok
                        print('Speech Recognition Stopped.')
                        break
                    elif str(recognizer.recognize_google(audio))=='add title':#ok
                        print(str(recognizer.recognize_google(audio)))
                        titl.delete(0,END)
                        # print('SpeakTitle:',end=' ')
                        b='t'
                        continue
                        # print(str(recognizer.recognize_google(audio)))
                        # titl.insert(END,str(recognizer.recognize_google(audio)))
                    elif str(recognizer.recognize_google(audio))=='add note':#ok
                        print(str(recognizer.recognize_google(audio)))
                        inp_note(str(titl.get()),str(InpNote.get("1.0",'end-1c')),str(rcolr[0]))
                        try:
                            titl.delete(first=0,last=END)
                        except:
                            print('No Title...')
                        InpNote.delete('1.0',END)
                    elif str(recognizer.recognize_google(audio))=='clear note':#ok
                        print(str(recognizer.recognize_google(audio)))
                        InpNote.delete('1.0',END)
                    elif str(recognizer.recognize_google(audio))=='add favourite':#ok
                        print(str(recognizer.recognize_google(audio)))
                        fav_note(str(titl.get()),str(InpNote.get("1.0",'end-1c')),str(rcolr[0]))
                        try:
                            titl.delete(first=0,last=END)
                        except:
                            print('No Title...')
                        InpNote.delete('1.0',END)
                    elif str(recognizer.recognize_google(audio))=='add reminder':#ok
                        print(str(recognizer.recognize_google(audio)))
                        defdat=datetime.now()
                        defseldate=defdat.strftime('%Y-%m-%d')
                        defseltime=defdat.strftime('%H:%M:%p')
                        print(defseldate,defseltime)
                        remindr(str(titl.get()),str(InpNote.get("1.0",'end-1c')),str(rcolr[0]),str(defseldate),str(defseltime))
                    elif str(recognizer.recognize_google(audio))=='dark mode':#ok
                        print(str(recognizer.recognize_google(audio)))
                        db.invoke()
                    elif str(recognizer.recognize_google(audio))=='light mode':#ok
                        print(str(recognizer.recognize_google(audio)))
                        lb.invoke()
                    else:#ok
                        print (recognizer.recognize_google(audio))
                        InpNote.insert(END,str(recognizer.recognize_google(audio))+' \n')                   
                        # print (recognizer.recognize_google_cloud(audio) )
                    b=''
                except Exception as e:
                    print(e,'.')
    Thread(target=micbt).start()

#done
#main window
root=ThemedTk(theme='breeze')#arc,equilux
root.title('SNORT:Smart Notes & Reminders')
root.geometry('350x500')
root.iconbitmap('ntsico.ico')

#darkmode
botton_frm=Frame(root,height=1)
botton_frm.pack(side=BOTTOM,fill=BOTH)

drk_photo=PhotoImage(file='drk.png')
lght_photo=PhotoImage(file='lght.png')
db=Button(botton_frm,image=drk_photo,bg='white',command=lambda:dark_md())
lb=Button(botton_frm,image=lght_photo,bg='white',command=lambda:light_md())
db.pack(side=RIGHT)
lb.pack(side=RIGHT)
#--CLOCK
def time(): 
    string = strftime('%H:%M:%S %p') 
    lbl.config(text = string) 
    lbl.after(1000, time)
lbl = Label(botton_frm, font = ('calibri', 20, 'bold')) 
lbl.pack(side=LEFT) 
time()

#tabs
tabControl=ttk.Notebook(root)
tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl) 
tab3 = ttk.Frame(tabControl) 

tabControl.add(tab1, text ='Notes') 
tabControl.add(tab2, text ='Favroites')
tabControl.add(tab3, text ='Reminders')
tabControl.pack(expand = 'yes', fill ="both") 

#Notes
lblfrm1=LabelFrame(tab1,text='(+)Add Notes',bg='#ffffff')
lblfrm1.pack(side=TOP,fill='both')

inp_notefrm_titl=Frame(lblfrm1,height=1)
inp_notefrm_note=Frame(lblfrm1)
inp_notefrm_optn=Frame(lblfrm1,height=1)

inp_notefrm_titl.pack(side=TOP,fill=BOTH)
inp_notefrm_note.pack(side=TOP,fill=BOTH)
inp_notefrm_optn.pack(side=TOP,fill=BOTH)

#note-title
lblTitl=Label(inp_notefrm_titl,text='Title:')
lblTitl.pack(side=LEFT,padx=2,pady=3)
titl=Entry(inp_notefrm_titl)
titl.pack(side=LEFT,fill=BOTH,expand=YES,padx=2,pady=3)

lbl1=Label(inp_notefrm_note,text='Note:')
lbl1.pack(side=LEFT,padx=1,pady=3)

#scroolbar
hn=Scrollbar(inp_notefrm_note,orient=VERTICAL)
hn.pack(side=RIGHT,fill=Y)

#enter-note
InpNote=Text(inp_notefrm_note,height=3,width=10)
InpNote.pack(side=LEFT,fill=BOTH,expand=YES,padx=2,pady=3)

micico=PhotoImage(file='microphone.png')
# mutico=PhotoImage(file='muted.png')

micbtn=Button(inp_notefrm_note,bg='#6ed8ff',image=micico,command=lambda : micon(True))##ceb0ff
micbtn.pack(side=LEFT,fill=Y,pady=3)
# mutbtn=Button(inp_notefrm_note,image=mutico,command=lambda : micon(False))
# mutbtn.pack(side=LEFT,fill=Y,pady=5)

#scroolbar
InpNote.configure(yscrollcommand = hn.set)
hn.config(command=InpNote.yview)

#icon-images
addbt=PhotoImage(file='plus.png')
favbt=PhotoImage(file='star.png')
imgbt=PhotoImage(file='picture.png')
reminbt=PhotoImage(file='school-bell1.png')

# delbt=PhotoImage(file='delete.png')
# editbt=PhotoImage(file='pencil.png')

#color picker
rcolr=[]
rcolr.append('white')
def callback():
    result = askcolor(title = "Tkinter Color Chooser")
    inp_notefrm_titl.configure(bg=result[1])
    inp_notefrm_note.configure(bg=result[1])
    inp_notefrm_optn.configure(bg=result[1])
    lstnts.configure(bg=result[1])
    bt.configure(bg=result[1])
    rcolr[0]=(result[1])
bt=Button(inp_notefrm_optn,command=callback,width=3,bg='#ffffff')
bt.pack(side=LEFT,fill=Y,padx=2,pady=3)

add_btn=Button(inp_notefrm_optn,image=addbt,bg='white',command=lambda:inp_note(str(titl.get()),str(InpNote.get("1.0",'end-1c')),str(rcolr[0])))
add_btn.pack(side=RIGHT,fill=BOTH,padx=2,pady=3)
fav_btn=Button(inp_notefrm_optn,image=favbt,bg='white',command=lambda:fav_note(str(titl.get()),str(InpNote.get("1.0",'end-1c')),str(rcolr[0])))
fav_btn.pack(side=RIGHT,fill=BOTH,padx=2,pady=3)
img_btn=Button(inp_notefrm_optn,image=imgbt,bg='white',command=lambda:ad_img(str(titl.get()),str(InpNote.get("1.0",'end-1c')),str(rcolr[0])))
img_btn.pack(side=LEFT,fill=BOTH,padx=2,pady=3)
    
#adding reminder to a note
def add_rem_tl():
    tlr=Toplevel()
    tlr.iconbitmap('dts.ico')
    tlr.title('Select date & time')

    tdy_frm=Frame(tlr,height=1)
    tdy_frm.pack(side=TOP)
    tdy=Label(tdy_frm,text=str(date.today()),font = ('calibri',20, 'bold'))
    tdy.pack(side=LEFT)

    ok_frm=Frame(tlr,height=1)
    ok_frm.pack(side=BOTTOM)
    ok_btn=Button(ok_frm,text='Done',command=lambda:[tlr.destroy(),remindr(str(titl.get()),str(InpNote.get("1.0",'end-1c')),str(rcolr[0]),seldate[0],seltim[0])])
    ok_btn.pack()

    #--CLOCK
    def time(): 
        string = strftime('%H:%M:%S %p') 
        lbl.config(text = string) 
        lbl.after(1000, time) 
    lbl = Label(tdy_frm, font = ('calibri',20, 'bold')) 
    lbl.pack(side=RIGHT) 
    time()

    #time
    lblHr=Label(tlr,text='Hour(12)')
    Hr=Entry(tlr,width=3)
    lblMin=Label(tlr,text='Minutes(60)')
    Min=Entry(tlr,width=3)
    lblAP=Label(tlr,text='AM/PM')
    AP=Entry(tlr,width=3)
    lblHr.pack(side=LEFT)
    Hr.pack(side=LEFT)
    lblMin.pack(side=LEFT)
    Min.pack(side=LEFT)
    lblAP.pack(side=LEFT)
    AP.pack(side=LEFT)
    
    
    #datepicker
    def dat_pic():
        def print_sel():
            print(cal.selection_get())
            seldate.append(str(cal.selection_get()))
            sel_dat=Label(tlr,text='Date:'+str(cal.selection_get()))
            sel_dat.pack(side=LEFT,fill=BOTH,expand=YES)
        dtselwin = Toplevel()
        dtselwin.iconbitmap('dts.ico')
        dtselwin.title('Select Date')
        cal = Calendar(dtselwin)
        cal.pack(fill="both", expand=TRUE,padx=10,pady=10)
        Button(dtselwin, text="Select", command=lambda:[dtselwin.destroy(),print_sel()]).pack()
        dtselwin.mainloop()
    def tim_pic():
        seltim.append(str(Hr.get())+':'+str(Min.get())+':'+str(AP.get()))
        print(seltim)
    ttk.Button(tlr,text='Select Time',command=tim_pic).pack(padx=10)
    ttk.Button(tlr, text='Select Date', command=dat_pic).pack(padx=10)
    tlr.mainloop()

remin_btn=Button(inp_notefrm_optn,image=reminbt,bg='white',command=add_rem_tl)
remin_btn.pack(side=RIGHT,fill=BOTH,padx=2,pady=3)

######
lblfrm12=LabelFrame(tab1,text='(|=|)List Notes',bg='#ffffff')
lblfrm12.pack(fill='both',expand='yes')
lstnts=Listbox(lblfrm12)
lstnts.pack(fill=BOTH,expand=TRUE)
lstscrlbr=Scrollbar(lstnts,orient=VERTICAL)
lstscrlbr.pack(side=RIGHT,fill=Y)
lstnts.configure(yscrollcommand = lstscrlbr.set)
lstscrlbr.configure(command=lstnts.yview)

lstscrlbrx=Scrollbar(lstnts,orient=HORIZONTAL)
lstscrlbrx.pack(side=BOTTOM,fill=X)
lstnts.configure(xscrollcommand = lstscrlbrx.set)
lstscrlbrx.configure(command=lstnts.xview)

#Reminders
lblfrm2=LabelFrame(tab3,text='Reminders')
lblfrm2.pack(fill='both',expand='yes')

#favroites
lblfrm3=LabelFrame(tab2,text='Favroites')
lblfrm3.pack(fill='both',expand='yes')
#root.wm_attributes("-topmost", 1)
root.mainloop()