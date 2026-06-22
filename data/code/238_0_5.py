import turtle

def draw_black_square():
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-50, 50)
    t.pendown()
    t.color("black")
    for _ in range(4):
        t.forward(100)
        t.right(90)

if __name__ == '__main__':
    draw_black_square()