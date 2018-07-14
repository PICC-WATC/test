from turtle import *
import time, random

l = 100
rotate = 144
delay = 0.01
screen = getscreen()
screen.tracer(0)
color("red")
while True:
	for i in range(3):
		fd(l)
		right(120)
	fd(5)
	if abs(pos()) > 250:
		rt(180)
	screen.update()
	time.sleep(delay)
	clear()