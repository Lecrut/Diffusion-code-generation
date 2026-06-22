import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

def calculate_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length ** 2

if __name__ == '__main__':
    try:
        circle_radius = 5
        square_side_length = 4
        circle_area = calculate_circle_area(circle_radius)
        square_area = calculate_square_area(square_side_length)
        total_area = circle_area + square_area
        print(total_area)
    except ValueError as e:
        print(e)