import turtle
def draw_triangle(side_length):
    t = turtle.Turtle()
    t.speed(5)
    t.pensize(2)
    t.color("blue")
    for _ in range(3):
        t.forward(side_length)
        t.left(120)
    turtle.done
if __name__ == '__main__':
    draw_triangle(150)