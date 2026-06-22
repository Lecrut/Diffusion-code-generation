import math

def calculate_areas():
    circle_area = math.pi * 5**2
    square_area = 4**2
    total_area = circle_area + square_area
    return total_area

if __name__ == '__main__':
    print(calculate_areas())