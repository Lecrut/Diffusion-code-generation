import math
AREA_TOLERANCE = 1e-09

def calculate_triangle_area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

def check_equal_area(triangle_coords, square_side_length):
    x1, y1 = triangle_coords[0]
    x2, y2 = triangle_coords[1]
    x3, y3 = triangle_coords[2]
    triangle_area = calculate_triangle_area(x1, y1, x2, y2, x3, y3)
    square_area = square_side_length ** 2
    return abs(triangle_area - square_area) < AREA_TOLERANCE
if __name__ == '__main__':
    triangle_coords = [(0, 0), (4, 0), (2, 3)]
    square_side_length = 5.65685424949
    print(check_equal_area(triangle_coords, square_side_length))