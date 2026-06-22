import turtle

def validate_side_length(side_length):
    if side_length <= 0:
        raise ValueError("Side length must be greater than zero")

def draw_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)

if __name__ == '__main__':
    try:
        validate_side_length(100)
        turtle.speed(1)
        draw_triangle(100)
        turtle.done()
    except ValueError as e:
        print(e)