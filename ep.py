from tkinter import *
import time
import random
from tkinter import ttk
from tkinter import messagebox as msgbox

#------------------------------------------------------------낚시 종류--------------------------------------------------------------------#
trash = ['거대한 운석','꼴등 복권','일등 복권','대관람차','나무뿌리','닌O도 스위치','나무 뿌리','밧줄','먹다남은 포O몬 빵','부러진 낚싯대','강아지 똥','안경닦이','낚시찌','코코넛 음료수','아크릴 판','비둘기 깃털']

general = ['잉어','금붕어','툭눈금붕어','메기','올챙이','닭새우','백미돔','열빙어','앨통이','청밀복','극지대구','클리오네','참치방어','얼룩매가오리','객주리','가자미','블루탱','전갱이']

rare = ['둥근논우렁이','난주','콩조개','다슬기','참붕어','황해볼락','둥근전복','민들조개','도미','문치가자미','수랑','꺽지']

superrare = ['점몰개','치리','밀어','눈동자개','다랑어','몰개']

junsul = ['묵납자루','흰고래','고양이고래','청새치','눈양태','좀수수치']

superjunsul = ['에우테놉테론','틱타알릭','사카밤바스피스','헬리코프리온','메갈로돈','니얼굴물고기']

god = ['3+3=6물고기']

#------------------------------------------------------------------낚시 문구----------------------------------------------------------------------#

fishtext = ['❗❗❗ 앗!!! 찌가 흔들린다!!!','❗❗❗ 앗!!! 낚시대가 요동친다!!!','❗❗❗ 앗!!! 지금이야!!!','❗❗❗ 앗!!! 바로 이 느낌!!!','❔❔❔ 갑자기 바람이 불어온다!!!','❔❔❔ 이건..?','❔❔❔ 어..갑자기 분위기가..뭔가 느낌이..!']
badtext = ['❗❗❗ 앗!!! 찌가 전혀 안 흔들린다!!!','❗❗❗ 앗!!! 낚시가 너무 재미있다!!!','❗❗❗ 앗!!! 오늘 날시 정말 최고!!!','❗❗❗ 앗!!! 윤이강은 잼민이다!!!']
normaltext = ['해물탕 먹고 싶다...','3+3=6이다...','날씨가 참 맑다...','오늘은 몇 마리 낚을 수 있을까...','아직 찌를 물지 않은 듯하다...']
#-------------------------------------------------------------------------------------------------------
size=['1.1','2,2','3.3','4.4','5.5','6.6','7.7']
#-----------------------------------------------start------------------------------------------------------#
with open('돈.txt','r') as file:
    gun=file.read()
if gun=='':
    with open('돈.txt','w') as file:
        file.write('0')
        
with open('명성.txt','r') as file:
    gun=file.read()
if gun=='':
    with open('명성.txt','w') as file:
        file.write('0')

with open('티어.txt','r') as file:
    gun=file.read()
if gun=='':
    with open('티어.txt','w') as file:
        file.write('1')

with open('땅.txt','w') as file:
    gun=file.read()
if gun=='':
    with open('땅.txt','w') as file:
        file.write('내땅아님')
#===============================================함수======================================================#
def fish(n):
    if n in fishtext:
        fish_percent = random.randint(1, 98979)
        if fish_percent < 5000:
            fishtype = random.choice(trash)
            fisi=float(random.choice(size))
            fisis=random.randint(10,700)
            fff=fisi*fisis
            msgbox.showinfo(f'{fishtype}을 낚아 버렸어...\n크기:{fff}\n종류:쓰레기')
        fishtype = 0
        elif fish_percent < 85000 and fish_percent > 5000:
            fishtype = random.choice(general)
            fisi=float(randonPym.choice(size))
            fisis=random.randint(10,700)
            fff=fisi*fisis
            money=fff*3
            star=money/10 +3
            msgbox.showinfo(f"{fishtype}가 낚였다!\n크기:{fff}\n종류:흔함\n돈:{money}\n명성:{star}")
            with open('돈.txt','r') as q:
                q.read()
                qq=int(q)+money
            with open('명성.txt','w') as qqq:
                qqq.write(qq)
            with open('명성.txt','r') as q:
                q.read()
                qq=int(q)+star
            with open('명성.txt','w') as qqq:
                qqq.write(qq)
        fishtype = 0
        elif fish_percent < 95000 and  fish_percent > 85000:
            fishtype = random.choice(rare)
            fisi=float(random.choice(size))
            fisis=random.randint(10,700)
            fff=fisi*fisis
            money=fff*7
            star=money/10 +3
            msgbox.showinfo (f"와!{fishtype}을 낚았다!\n크기:{fff}\n종류:귀함\n돈:{money}\n명성:{star}")
            with open('돈.txt','r') as q:
                q.read()
                qq=int(q)+money
            with open('명성.txt','w') as qqq:
                qqq.write(qq)
            with open('명성.txt','r') as q:
                q.read()
                qq=int(q)+star
            with open('명성.txt','w') as qqq:
                qqq.write(qq)
        fishtype = 0
        elif fish_percent < 98000 and  fish_percent > 95000:
            fishtype = random.choice(superrare)
            fisi=float(random.choice(size))
            fisis=random.randint(10,700)
            fff=fisi*fisis
            money=fff*20
            star=money/10 +3
            msgbox.showinfo (f"월척이야!{fishtype}을 낚다니!\n크기:{fff}\n종류:매우귀함\n돈:{money}\n명성:{star}")
            with open('돈.txt','r') as q:
                q.read()
                qq=int(q)+money
            with open('명성.txt','w') as qqq:
                qqq.write(qq)
            with open('명성.txt','r') as q:
                q.read()
                qq=int(q)+star
            with open('명성.txt','w') as qqq:
                qqq.write(qq)
        fishtype = 0
        elif fish_percent < 98800 and  fish_percent > 98000:
            fishtype = random.choice(junsul)
            fisi=float(random.choice(size))
            fisis=random.randint(10,700)
            fff=fisi*fisis
            money=fff*50
            star=money/10 +3
            msgbox.showinfo (f"이건..{fishtype}잖아?!?!\n크기:{fff}\n종류:전설\n돈:{money}\n명성:{star}")
            with open('돈.txt','r') as q:
                q.read()
                qq=int(q)+money
            with open('명성.txt','w') as qqq:
                qqq.write(qq)
            with open('명성.txt','r') as q:
                q.read()
                qq=int(q)+star
            with open('명성.txt','w') as qqq:
                qqq.write(qq)
        fishtype = 0
        elif fish_percent < 98900 and  fish_percent > 98800:
            fishtype = random.choice(superjunsul)
            fisi=float(random.choice(size))
            fisis=random.randint(10,700)
            fff=fisi*fisis
            money=fff*100
            star=money/10 +3
            msgbox.showinfo (f"{fishtype}라고?!가능한 거야??\n크기:{fff}\n종류:초전설\n돈:{money}\n명성:{star}")
            with open('돈.txt','r') as q:
                q.read()
                qq=int(q)+money
            with open('명성.txt','w') as qqq:
                qqq.write(qq)
            with open('명성.txt','r') as q:
                q.read()
                qq=int(q)+star
            with open('명성.txt','w') as qqq:
                qqq.write(qq)
        fishtype = 0
        elif fish_percent < 98970 and  fish_percent > 98900:
            fishtype = random.choice(god)
            fisi=float(random.choice(size))
            fisis=random.randint(10,700)
            fff=fisi*fisis
            money=fff*200
            star=money/10 +3
            msgbox.showinfo (f"와..{fishtype}이라니..!복권사야겠다!!\n크기:{fff}\n종류:갓\n돈:{money}\n명성:{star}")
            with open('돈.txt','r') as q:
                q.read()
                qq=int(q)+money
            with open('명성.txt','w') as qqq:
                qqq.write(qq)
            with open('명성.txt','r') as q:
                q.read()
                qq=int(q)+star
            with open('명성.txt','w') as qqq:
                qqq.write(qq)
    else:
        msgbox.showinfo("[낚시 실패]\n찌를 올렸지만 아무것도 없었다...")


def stop():
    msgbox.showinfo("낚싯대를 감아 정리했다.")

#--------------------------------------------------------

def buy():
    f=open('돈.txt','w')
    read=f.readline()
    if read=='' or int(read)<30000:
        msgbox.showerror('돈이 부족합니다.(매입가 30000원)')
        f.close()
    else:
        read2=(int(read))-30000
        f.write(str(read2))
        f.close()
        c=open('땅.txt','w')
        c.write('내땅')
        c.close()

def sell():
    f=open('땅.txt','w')
    read=f.readline()
    if read=='내땅아님':
        msgbox.showerror('이미 내 땅이 아닙니다.')
    if read=='':
        f.write('0')
    else:
        read2=(int(read))+30000
        f.write(str(read2))
        f.close()
        c=open('땅.txt','w')
        c.write('내땅아님')
        c.close()

def lank():
    with open('돈.txt','w') as lanking:
        lank=int(lanking.read())
    if 0<lank and lank<50000:
        la='beginner'
    if 50000<lank and lank<100000:
        la='newbie'
    if 100000<lank and lank<300000:
        la='grinder'
    if 300000<lank and lank<600000:
        la='master'
    if 600000<lank and lank<1000000:
        la='pro fisher'
    if 1000000<lank and lank<10000000:
        la='ranker'
    if 10000000<lank and lank<100000000:
        la='impossible fisher'
    if 100000000<lank
        la='god fisher'
    with open('돈.txt','w') as l:
        l.write(str(la))
    lank=Toplevel()
    lbbb = Label(lank, text = f"내 랭크: {la}")
    lbbb.pack()
    
def up():
     with open('명성.txt','w') as wi:
        w=int(wi.read())
        if w<5000:
            msgbox.showerror('돈이 부족합니다.(5000명성 필요')
        else:
            ww=w-5000
            wi.write(str(ww))
            with open('티어.txt','w') as op:
                o=op.read()
            if o=='':
                ooo='1'
            else:
                oo=int(o)
                ooo=oo+1
                msgbox.showinfo(f'낚시터가 업그레이드되었습니다!\n현재 낚시터레벨:{ooo}티어')
                with open('명성.txt','w') as opp:
                    opp.write(str(ooo))
    
def down():
    with open('명성.txt','w') as wi:
        w=int(wi.read())
        ww=w+5000
    with open('명성.txt','w') as ori:
            ori.write(str(ww))
        with open('티어.txt','w') as op:
            o=op.read()
        if o=='':
            ooo='1'
            msgbox.showinfo('현재 낚시터가 1티어이기 때문에 다운그레이드 할수 없습니다..')
            with open('명성.txt','w') as oop:
                oop.write('1')
        else:
                o=int(o)
            ooo=oo-1
            msgbox.showinfo(f'낚시터가 다운그레이드되었습니다!\n현재 낚시터레벨:{ooo}티어')
            with open('티어.txt','w') as opp:
                opp.write(str(ooo))
            
def gehung():
    f=open('땅.txt','w')
    read=f.readline()
    if read=='내땅':
        def on_select(event):
            selected_value = n.get()
            with open('지형.txt','w') as yoon:
                yoon.write(str(selected_value))
                msgbox.showinfo('낚시터 지형이 변경되었습니다.')

        window = Tk()
        window.geometry('500x500')

        lb = Label(window, text="지형 선택:", font=("Times New Roman", 10))
        lb.grid(column=0, row=5, padx=10, pady=25)

        n = StringVar()
        strb = ttk.Combobox(window, width=27, textvariable=n)
        strb['values'] = ('🏜 메마른 땅', '🏖 바닷가', '🏞 강가', '🚤 호수', '⛰ 계곡', '🥬 습지', '🦀 갯벌')
        strb.grid(column=1, row=5)
        strb.current()

        strb.bind("<<ComboboxSelected>>", on_select)

        window.mainloop()
    else:
        msgbox.showerror('내 땅이 아닙니다.')

def information():
    he = Toplevel()
    he.geometry("300x300")
    he.title("낚시터 정보")
    alist=['봄','여름','가을','겨울']
    ge=random.choice(alist)
    with open('지형.txt','r') as yoon:
        yy=yoon.read()
    with open('티어.txt','r') as op:
        o=op.read()
    with open('명성.txt','r') as mung:
        mm=mung.read()
    #청결도 등
    lb = Label(he, text = f"<계절> {ge}")
    lb.pack()
    lbb = Label(he, text = f"<지형> {yy}")
    lbb.pack()
    lbbbb=Label(he, text = f"<낚시터 명성> {mm}")
    lbbb = Label(he, text = f"<낚시터 티어> {o}")
    lbbb.pack()

       
#--------------------------------------------------------

def randomtext():
    global f
    for i in range(15):
        f=random.randint(1,10)
        if f<8:
            f=random.choice(normaltext)
            print(f)
        elif f==8 or f==9:
            f=random.choice(fishtext)
            print(f)
        else:
            f=random.choice(badtext)
            print(f)
        
        time.sleep(2)
    msgbox.showinfo("[낚시 실패]\n자리를 잘못 잡았나...?")

def fishs():
    fish(f)

def toplevel():
    oh=Toplevel()
    oh.geometry('400x400')
    oh.title('낚시')
    btn = Button(oh, text="🎣낚싯줄 당기기",command=fishs)
    btn.place(x=100,y=300)
    
    btn = Button(oh, text="그만하기",command=stop)
    btn.place(x=220,y=300)

def booost():
    with open('명성.txt','r') as p:
        p.read()
        if int(p)<10000:
            msgbox.showerror('명성이 부족합니다.')
        else:
            pp=int(p)-10000
            msgbox.showinfo('부스트 완료!')
            p.write(str(pp))
            with open('부스트.txt','w') as bo:
                bo.write('부스트')

def boost():
    oh=Toplevel()
    oh.geometry('400x400')
    oh.title('boost')
    btn = Button(oh, text="명성 10000필요\n이 낚시터 부스트하기\n(주의사항:부스트는 중첩되지 않습니다.)",command=booost)
    btn.pack()
    quail=Label(oh,text='효과:낚시 낚일확률 20%증가(쓰레기포함)')
    quail.pack()
#----------------------------------------메인창--------------------------------------

root =Tk()
root.geometry('400x30')
root.title("낚시")

mb=Menu(root)

m = Menu(mb, tearoff=0)
m.add_command(label='낚시터 정보',command = information)
m.add_command(label='낚시터 매입',command = buy)
m.add_command(label='낚시터 매각',command = sell)
m.add_command(label='낚시터 업그레이드',command = up)
m.add_command(label='낚시터 다운그레이드',command = down)
m.add_command(label='낚시터 지형변경',command = gehung)
mb.add_cascade(label="낚시터", menu=m)

mm = Menu(mb, tearoff=0)
m.add_command(label='랭크',command = lank)
mb.add_cascade(label="내정보", menu=mm)

mmm = Menu(mb, tearoff=0)
m.add_command(label='낚시터 부스트',command = boost)
mb.add_cascade(label="부스트", menu=mmm)

root.config(menu=mb)
    
root.mainloop()

