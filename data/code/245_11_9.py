def calculate_triangle_area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0)

def calculate_square_area(side_length):
    return side_length ** 2

def check_equal_areas(triangle_coords, square_side_length, tolerance=1e-9):
    area_triangle = calculate_triangle_area(*triangle_coords)
    area_square = calculate_square_area(square_side_length)
    return abs(area_triangle - area_square) < tolerance

if __name__ == '__main__':
    triangle_coords = (0, 0), (4, 0), (2, 3)
    square_side_length = 3.5
    result = check_equal_areas(triangle_coords, square_side_length)
    print(result)