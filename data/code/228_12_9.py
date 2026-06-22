import turtle

def draw_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)

if __name__ == '__main__':
    try:
        side_length = 100
        if side_length <= 0:
            raise ValueError("Side length must be greater than zero")
        turtle.speed(1)
        draw_triangle(side_length)
        turtle.done()
    except ValueError as e:
        print(e)