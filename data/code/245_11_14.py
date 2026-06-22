import math

def calculate_triangle_area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0)

def check_equal_area(triangle_coords, square_side_length):
    tolerance = 1e-9
    area_triangle = calculate_triangle_area(*triangle_coords)
    area_square = square_side_length ** 2
    return abs(area_triangle - area_square) < tolerance

if __name__ == '__main__':
    triangle_coords = (0, 0), (4, 0), (2, 3)
    square_side_length = 5.656854249492381
    print(check_equal_area(triangle_coords, square_side_length))