import turtle

def draw_black_square():
    t = turtle.Turtle()
    t.speed(0)
    t.fillcolor("black")
    t.begin_fill()
    for _ in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()

if __name__ == '__main__':
    draw_black_square()