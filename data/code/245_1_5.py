import math

def compare_areas(circle_radius, square_side):
    circle_area = math.pi * (circle_radius ** 2)
    square_area = square_side ** 2
    if circle_area > square_area:
        return "Circle"
    elif circle_area < square_area:
        return "Square"
    else:
        return "Equal"

if __name__ == '__main__':
    print(compare_areas(5, 8))