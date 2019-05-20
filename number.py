import random

r = random.randint(1, 100)
c = 0
while True:
	c = c + 1
	a = input('請猜大小：')
	a = int(a)
	if a == r:
	    print('終於猜對了！這是你猜的第', c,'次！')
	    break
	elif a < r:
	    print('比答案小, 這是你猜的第', c,'次！')
	elif a > r:
	    print('比答案大，這是你猜的第', c,'次！')