import random
minr = int(input("請輸入最小值:"))
maxr = int(input("請輸入最大值:"))
time = 0
r = random.randint(minr, maxr)
while True :
    time += 1
    answer = int(input("請輸入範圍之間的數字:"))
    if r > answer :
        print("比答案小")
    elif r == answer :
        print("答對了!")
        break
    else :
        print("比答案大")
print("總共猜了%d次"%time)