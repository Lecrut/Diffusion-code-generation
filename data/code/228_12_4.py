import turtle

def draw_equilateral_triangle(side_length):
    if side_length <= 0:
        raise ValueError("Side length must be greater than zero")
    
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)

if __name__ == '__main__':
    try:
        turtle.speed(1)
        draw_equilateral_triangle(100)
        turtle.done()
    except ValueError as e:
        print(e)