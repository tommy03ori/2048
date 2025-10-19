import random
import numpy as np
# 2048を手動で実装するチャレンジ

def reset_bord():
    '''
    盤面をリセット
    '''
    bord = np.zeros((4, 4), dtype='int64')
    bord = new_num_place(bord)
    return bord

def new_num_place(bord):
    '''
    ボード上の任意の空きマスに新しく2を導入
    '''
    while True:
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        if bord[y, x] == 0:
            bord[y, x] = 2
            break
    return bord

def up(bord):
    '''
    上にフリックされたときの処理
    '''
    # 上方向につめつめにする（合体はしない）
    for _ in range(3):
        # どんな盤面でも3回つめればつめつめになる（power implemention）
        for y in range(1, 4):
            for x in range(4):
                if bord[y, x] != 0 and bord[y-1, x] == 0:
                    bord[y-1, x] = bord[y, x]
                    bord[y, x] = 0
    # 同じ数字はくっつける
    for y in range(1, 4):
        for x in range(4):
            if bord[y, x] == bord[y-1, x]:
                bord[y-1, x] *= 2
                bord[y, x] = 0
    # 最後にもう一回つめつめにする
    for y in range(1, 4):
        for x in range(4):
            if bord[y, x] != 0 and bord[y-1, x] == 0:
                bord[y-1, x] = bord[y, x]
                bord[y, x] = 0
    bord = new_num_place(bord)
    return bord

def left(bord):
    '''
    左にフリックされたときの処理
    '''
    # 左方向につめつめにする（合体はしない）
    for _ in range(3):
        # どんな盤面でも3回つめればつめつめになる（power implemention）
        for x in range(1, 4):
            for y in range(4):
                if bord[y, x] != 0 and bord[y, x-1] == 0:
                    bord[y, x-1] = bord[y, x]
                    bord[y, x] = 0
    # 同じ数字はくっつける
    for x in range(1, 4):
        for y in range(4):
            if bord[y, x] == bord[y, x-1]:
                bord[y, x-1] *= 2
                bord[y, x] = 0
    # 最後にもう一回つめつめにする
    for x in range(1, 4):
        for y in range(4):
            if bord[y, x] != 0 and bord[y, x-1] == 0:
                bord[y, x-1] = bord[y, x]
                bord[y, x] = 0
    bord = new_num_place(bord)
    return bord

def down(bord):
    # 下方向につめつめにする（合体はしない）
    for _ in range(3):
        # どんな盤面でも3回つめればつめつめになる（power implemention）
        for y in range(2, -1, -1):
            for x in range(4):
                if bord[y, x] != 0 and bord[y+1, x] == 0:
                    bord[y+1, x] = bord[y, x]
                    bord[y, x] = 0
    # 同じ数字はくっつける
    for y in range(2, -1, -1):
        for x in range(4):
            if bord[y, x] == bord[y+1, x]:
                bord[y+1, x] *= 2
                bord[y, x] = 0
    # 最後にもう一回つめつめにする
    for y in range(2, -1, -1):
        for x in range(4):
            if bord[y, x] != 0 and bord[y+1, x] == 0:
                bord[y+1, x] = bord[y, x]
                bord[y, x] = 0
    bord = new_num_place(bord)
    return bord

def right(bord):
    # 右方向につめつめにする（合体はしない）
    for _ in range(3):
        # どんな盤面でも3回つめればつめつめになる（power implemention）
        for x in range(2, -1, -1):
            for y in range(4):
                if bord[y, x] != 0 and bord[y, x+1] == 0:
                    bord[y, x+1] = bord[y, x]
                    bord[y, x] = 0
    # 同じ数字はくっつける
    for x in range(2, -1, -1):
        for y in range(4):
            if bord[y, x] == bord[y, x+1]:
                bord[y, x+1] *= 2
                bord[y, x] = 0
    # 最後にもう一回つめつめにする
    for x in range(2, -1, -1):
        for y in range(4):
            if bord[y, x] != 0 and bord[y, x+1] == 0:
                bord[y, x+1] = bord[y, x]
                bord[y, x] = 0
    bord = new_num_place(bord)
    return bord


def main():
    '''
    本体
    '''
    bord = reset_bord()
    print(bord)
    while True:
        ipt = input()
        if ipt == "q":
            return
        elif ipt == "h":
            print("Help\n  w: up\n  a: left\n  s: down\n  d: right")
        else:
            if ipt == "w":
                bord = up(bord)
            if ipt == "a":
                bord = left(bord)
            if ipt == "s":
                bord = down(bord)
            if ipt == "d":
                bord = right(bord)
            print(bord)

main()
            

