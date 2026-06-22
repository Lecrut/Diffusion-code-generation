import math

def calculate_triangle_area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0)

def calculate_square_area(side_length):
    return side_length ** 2

def check_equal_area(triangle_coords, square_side_length):
    if not (isinstance(triangle_coords, tuple) and len(triangle_coords) == 6):
        raise ValueError("Triangle coordinates must be a tuple of six numbers")
    if not isinstance(square_side_length, (int, float)) or square_side_length <= 0:
        raise ValueError("Square side length must be a positive number")

    triangle_area = calculate_triangle_area(*triangle_coords)
    square_area = calculate_square_area(square_side_length)

    tolerance = 1e-9
    return abs(triangle_area - square_area) < tolerance

if __name__ == '__main__':
    triangle_coords = (0, 0, 4, 0, 2, 3)
    square_side_length = 5.656854249492381
    print(check_equal_area(triangle_coords, square_side_length))