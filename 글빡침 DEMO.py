import tkinter as tk
import time

wryn = 0
gg = []
mcount = 0

root = tk.Tk()
root.title("this is untitled!")
root.geometry("800x700")
root.resizable(True, False)

text_frame = tk.Frame(root)
text_frame.pack(padx=15, pady=15, fill="both", expand=True)

scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side="right", fill="y")

text_box = tk.Text(
    text_frame,
    font=("Comic Sans MS", 12),
    wrap="word",
    state="disabled",
    yscrollcommand=scrollbar.set
)
text_box.pack(side="left", fill="both", expand=True)

scrollbar.config(command=text_box.yview)

button_frame = tk.Frame(root, height=170)
button_frame.pack(padx=10, pady=10, fill="x")
button_frame.pack_propagate(False)

choice_buttons = []
choice_var = tk.StringVar()


def hide_buttons():
    for button in choice_buttons:
        button.grid_remove()


def clear_buttons():
    for button in choice_buttons:
        button.destroy()
    choice_buttons.clear()


def say(speed, text=''):

    if isinstance(speed, str):
        text = speed
        speed = 0.05  
    hide_buttons()

    text_box.config(state="normal")

    if text_box.get("1.0", tk.END).strip() != "":
        text_box.insert(tk.END, "\n\n")

    for ch in text:
        text_box.insert(tk.END, ch)
        text_box.see(tk.END)
        root.update()
        time.sleep(speed)

    text_box.config(state="disabled")

def make_choices(*choices):
    clear_buttons()
    choice_var.set("")

    choices = choices[:15]

    for i, choice in enumerate(choices):
        row = i // 5
        col = i % 5

        button = tk.Button(
            button_frame,
            text=choice,
            width=20,
            height=2,
            font=("Comic Sans MS", 10),
            command=lambda c=choice: choice_var.set(c)
        )

        button.grid(row=row, column=col, padx=5, pady=5)
        choice_buttons.append(button)

    root.wait_variable(choice_var)

    selected = choice_var.get()
    clear_buttons()

    return selected

def game_over(restart=None):
    button = tk.Button(
            button_frame,
            text='재시도',
            width=20,
            height=2,
            font=("Comic Sans MS", 10),
            command=game
        )
    button.grid(row=0, column=0, padx=5, pady=5)
    choice_buttons.append(button)

    root.wait_variable(choice_var)

    selected = choice_var.get()
    clear_buttons()
def game():
    #모아이 일정 점수 시 업그레이드 가능, 점수가 많을시 엔딩 추가.
    global gg
    choices = make_choices('알겠소','엔딩들 보기','모아이 클리커')
    if choices == '엔딩들 보기':
        say('현재 보유 엔딩: {}'.format(gg))
        game_over()
    elif choices == '모아이 클리커':
        while True:
            global mcount
            say(str(mcount))
            choiceM = make_choices('🗿','끝내기')
            if choiceM == '🗿':
                mcount += 1
                continue
            elif choiceM == '끝내기':
                game_over()
            else:
                print('')
    elif choices == '알겠소':
        start_time = time.time()
        say('지금 현재 시각 2시 10분. 어떻게 할 것인가?')
        choice1 = make_choices('밖에 나가기','더 자기','팔을 미친 것처럼 빙빙 돌리기')
        if choice1 == '밖에 나가기':
            say('밖에 나가니 시원하다.')
            say('이런! 바람에 날라가 버렸다!')
            end_time = time.time()
            say('새로운 엔딩 해금!\n오즈의 마법사\n"도로시는 미국 캔자스주의 드넓은 평원에서, 농부인 헨리 아저씨와 아저씨의 아내인 엠 아줌마와 함께 살았다."')
            print('========================================')
            gg.append('오즈의 마법사')
            game_over()
        elif choice1 == '더 자기':
            say('잠에 든다..')
            say('이런! 배게에 껴서 질식했다!')
            end_time = time.time()
            say('새로운 엔딩 해금!\n질식사\n"얘들아, 배게가 이렇게 위험하단다."')
            print('========================================')
            gg.append('질식사')
            game_over()
        elif choice1 == '팔을 미친 것처럼 빙빙 돌리기':
            say('투두두두두두. 넌 빙빙 돌고 있다.')
            choice2 = make_choices('밖에 나가기','더 자기')
            if choice2 == '밖에 나가기':
                say('투두두두. 넌 바람에 타서 날고 있다.')
                say('침대리오의 집(옆집)까지 순식관(🤫)에 도착했다!')
                say('\"와후! 나의 이름은 ⓜ리오지만 넌 날 침대리오라 불러야 돼지\"')
                choice3 = make_choices('침대리오', 'ⓜ리오','GIGACHAD🗿🗿🗿🗿🗿🗿🗿')
                if choice3 == '침대리오':
                    say('불러야 돼지')
                    say('러야 돼지')
                    say('야 돼지')
                    say('의사양반, 그게 무슨 소리요..?')
                    say('\"넌 돼지다\"')
                    say('내.. 내가 돼지라니!!!!!!!')
                    end_time = time.time
                    say('새로운 엔딩 해금!\n돼지\n"내.. 내가 돼지라니!!!!"')
                    print('=======================================')
                    gg.append('돼지')
                    game_over()
                elif choice3 == 'ⓜ리오':
                    say('이런! 저작권의 킹 Mr.판사가 나타났다!')
                    say('미안하네. 난 진짜 Mr.판사가 아니라네. 진짜 Mr.판사는 다음 업데이트때 올 거야.')
                    game_over()
                elif choice3 == 'GIGACHAD🗿🗿🗿🗿🗿🗿🗿':
                    say('🤫🤫🤫🤫🤫🤫🤫🤫🤫🤫🤫🤫🤫🤫🗿🗿🗿🗿🗿🗿🗿🗿')
                    say('좀 치네? 여기 이걸 주겠네.')
                    say('미스터리한 티켓을 얻었다.')
                    choice4 = make_choices('티켓 사용','티켓을 먹기','티켓을 변기에 넣기')
                    if choice4 == '티켓을 먹기':
                        say('하지만 당신은 방사성 인간이었다. 티켓을 물자 티켓이 인간티켓으로 변했다!')
                        end_time = time.time
                        say('새로운 엔딩 해금!\n인간티켓\n"그는 슈퍼히어로가 되었다 전해진다."')
                        gg.append('인간티켓')
                        game_over()
                    elif choice4 == '티켓을 변기에 넣기':
                        say('변기에 넣기도 전에 당신은 엄청난 ⓓ냄새를 맞고 쓰러졌습니다.')
                        end_time = time.time
                        say('새로운 엔딩 해금!\n이게 무슨\n"아 미안 그거 내꺼야\n-침대리오"')
                        gg.append('이게 무슨')
                        game_over()
                    elif choice4 == '티켓 사용':
                        say('당신은 순식간에 비행기로 텔포되었다!')
                        say('이 비행기는\n이스터 섬으로 간다.')
                        say('모아이 만나러 가자아아아아아아아아!!!!!!!!!!!')
                        say('데모 끝')
                        game_over()
                    else:
                        say('p')  
                else:
                    say('poop')
            elif choice2 == '더 자기':
                say('자려고 침대에 눕는다.')
                say('이런! 침대가 마하 5의 속도로 돌고 있는 너의 팔에 갈렸다!')
                say('이런! 침대리우스(너의 침대)의 형 침대리오가 나타났다!')
                say('이런! 넌 복수를 당해서 감옥에 갇혔다!')
                end_time = time.time()
                say('새로운 엔딩 해금!\n수감\n"[쇼생크], 여길 [탈출]해 보는 건 어때?"')
                print('========================================')
                gg.append('수감')
                game_over()
            else:
                say('poop')
        else:
            say('poop')
say('뉴그라운즈의 \'The Impossible quiz\'에게서 영감을 받았다.')
say('글빡침')
game()
