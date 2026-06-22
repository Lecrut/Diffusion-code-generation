def triangle_area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0)

def square_area(side_length):
    return side_length ** 2

def compare_areas(triangle_coords, square_side, tolerance=1e-9):
    t_x1, t_y1, t_x2, t_y2, t_x3, t_y3 = triangle_coords
    tri_area = triangle_area(t_x1, t_y1, t_x2, t_y2, t_x3, t_y3)
    sq_area = square_area(square_side)
    return abs(tri_area - sq_area) < tolerance

if __name__ == '__main__':
    print(compare_areas((0, 0, 4, 0, 2, 3), 5))