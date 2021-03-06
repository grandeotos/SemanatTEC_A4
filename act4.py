"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.

"""

from random import randrange, choice
from turtle import *
from freegames import vector

ball = vector(-1000, -1000)
speed = vector(0, 0)
targets = []
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 3
        speed.y = (y + 200) / 3

def inside(xy):
    "Return True if xy within screen."
    return -3000 < xy.x < 3000 and -3000 < xy.y < 3000

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, choice(colors))
    
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, choice(colors))

    update()

def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.9 # Rapido el target

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
        

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 10)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()