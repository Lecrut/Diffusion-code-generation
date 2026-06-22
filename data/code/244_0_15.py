import math

def compute_circle_area(radius):
    return math.pi * radius ** 2

def compute_square_area(side_length):
    return side_length ** 2

def sum_areas(circle_radius, square_side_length):
    circle_area = compute_circle_area(circle_radius)
    square_area = compute_square_area(square_side_length)
    total_area = circle_area + square_area
    return total_area

if __name__ == '__main__':
    sample_circle_radius = 5
    sample_square_side_length = 4
    result = sum_areas(sample_circle_radius, sample_square_side_length)
    print(result)