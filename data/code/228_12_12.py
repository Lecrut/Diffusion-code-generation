import turtle

def draw_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)

if __name__ == '__main__':
    triangle_side = 100
    turtle.speed(1)
    draw_triangle(triangle_side)
    turtle.done()