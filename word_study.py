import sys
import random

#復習回数の入力
while True:
    try:
        n = int(input("何問復習しますか？ > "))
    except:
        print("数値を入力してください。")
    else:
        break

#覚えた英単語や漢字、と意味を入力する
word_dic = {}
for i in range(0,n):
    word = input(f"復習したい単語を{n}個まで入力。登録済: {i}個、中断:1、終了:9 > ")
    
    if word.isalpha():
        word_dic[word] = input(f"{word}の意味を入力 > ")
    else:
        if int(word) == 1:
            print(f"入力の中断、復習単語：{i}個")
            break
        elif int(word) == 9:
            print("プログラムを終了します")
            sys.exit()

print(f"\n登録した内容：{i + 1}個\n{word_dic}\n")

#入力した内容で、復習ゲーム
print("登録内容で復習ゲームを始めます。パス：1、終了：9")


#辞書をタプルに入れる
words = tuple(word_dic.items())

#乱数生成
lrnd = [i for i in range(len(words))]
lrnd = random.sample(lrnd,len(words))


#★メモ：単語と意味をバラバラに問う、ごちゃまぜ復習モードも追加したい

cnt = 0         #正解カウント
incorrect = 0   #不正解カウント
ans_dict = {}   #出題内容を入れる

# =========================================== ゲーム開始
while cnt < len(words):
    
    ans = input(f"{words[lrnd[cnt]][0]}の意味を入力：> ")
    
    #入力値判定
    if ans.isalpha():
       #正解
        if ans == words[lrnd[cnt]][1]:
            print("正解です！")
            ans_dict[words[lrnd[cnt]][0]] = incorrect
            cnt += 1
            incorrect = 0   #不正解リセット
        #不正解
        else:
            print("不正解です…")
            incorrect += 1

    else:  
        #９の入力時はゲーム終了
        if int(ans) == 9:
            break
        else:
        #その他の数値はパス
            print("パス")
            ans_dict[words[lrnd[cnt]][0]] = "パス"
            cnt += 1
            incorrect = 0   #不正解リセット
else:
    print(f"\n結果：「出題：正答数」>\n{ans_dict}")

print("ゲームを終了しました。")