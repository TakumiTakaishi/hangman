import random

def hangman(word):
    turn = 1
    wrong = 0
    stages = ["\ Help me! /",
             "______      ",
             "|     |     ",
             "|     O     ",
             "|    /|\    ",
             "|     |     ",
             "|    / \    ",
             "|           ",
             ]
    corrects = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    
    while wrong < len(stages) - 1:
        
        # アルファベットの入力
        print(f"\n====== {turn}ターン目 ======")
        print(" ".join(board))
        char = input("当てはまるアルファベットを1文字予想してね：")
        
        # 入力されたアルファベットの判定
        if char in corrects:
            char_index = corrects.index(char)
            board[char_index] = char
            corrects[char_index] = "$"
            turn += 1
        else:
            wrong += 1
            turn += 1
        
        # 勝ち判定
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
            
    # 負け判定
    if not win :
        print(f"あなたの負け！ 正解は {word} でした！")

words = ["category", "homework", "smart", "latest", "overall", "security", "clean", "weekend"]
random = random.randint(0,len(words)-1)
hangman(words[random])