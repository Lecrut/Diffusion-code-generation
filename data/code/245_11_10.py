def triangle_area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0)

def square_area(side_length):
    return side_length ** 2

def compare_areas(triangle_coords, square_side_length, tolerance=1e-9):
    triangle = triangle_area(*triangle_coords)
    square = square_area(square_side_length)
    return abs(triangle - square) <= tolerance

if __name__ == '__main__':
    print(compare_areas((0, 0), (4, 0), (2, 3)))