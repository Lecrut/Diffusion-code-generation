import math

def compare_areas(circle_radius, square_side):
    circle_area = math.pi * (circle_radius ** 2)
    square_area = square_side ** 2
    return circle_area, square_area

if __name__ == '__main__':
    circle_radius = 5
    square_side = 7
    circle_area, square_area = compare_areas(circle_radius, square_side)
    print(f"Circle area: {circle_area}, Square area: {square_area}")