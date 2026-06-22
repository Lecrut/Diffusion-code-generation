import math

def calculate_area():
    circle_radius = 5
    square_side = 4
    circle_area = math.pi * (circle_radius ** 2)
    square_area = square_side ** 2
    total_area = circle_area + square_area
    return total_area

if __name__ == '__main__':
    print(calculate_area())