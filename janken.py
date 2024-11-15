import random

def Janken(a, b, kaisu):
    a_wincount = 0
    b_wincount = 0
    
    def hand(num):
        if num == 0:
            return "グー"
        elif num == 1:
            return "チョキ"
        else:
            return "パー"
    
    for i in range(kaisu):
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        
        hand1 = hand(x)
        hand2 = hand(y) 
        
        if x == y:
            print(a + "の手: " + hand1 + " v.s." + b + "の手: " + hand2 + " -> 引き分け")
        elif (x == 0 and y == 1) or (x == 1 and y == 2) or (x == 2 and y == 0):
            a_wincount += 1
            print(a + "の手: " + hand1 + " v.s." + b + "の手: " + hand2 + " -> " + a + "の勝ち")
        else:
            b_wincount += 1
            print(a + "の手: " + hand1 + " v.s." + b + "の手: " + hand2 + " -> " + b + "の勝ち")

    if a_wincount == b_wincount:
        print("結果 : 引き分け")
    elif a_wincount > b_wincount:
        print("結果 : " + a + "の勝ち")
    else:
        print("結果 : " + b + "の勝ち")

player1 = "A"
player2 = "B"

kaisu = 3

Janken(player1, player2, kaisu)