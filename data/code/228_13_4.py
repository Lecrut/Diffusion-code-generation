def get_triangle_coordinates(x1, y1, x2, y2, x3, y3):
    return [(x1, y1), (x2, y2), (x3, y3)]

if __name__ == '__main__':
    print(get_triangle_coordinates(0, 0, 1, 0, 0, 1))