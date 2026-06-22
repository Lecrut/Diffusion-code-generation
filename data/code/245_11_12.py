import math

def calculate_triangle_area(x1, y1, x2, y2, x3, y3):
    return abs(0.5 * (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)))

def calculate_square_area(side_length):
    return side_length ** 2

def check_equal_area(x1, y1, x2, y2, x3, y3, side_length):
    triangle_area = calculate_triangle_area(x1, y1, x2, y2, x3, y3)
    square_area = calculate_square_area(side_length)
    tolerance = 1e-9
    return abs(triangle_area - square_area) < tolerance

if __name__ == '__main__':
    print(check_equal_area(0, 0, 4, 0, 2, 3, 5))