def print_shape_repeated(coords):
    x1, y1, x2, y2 = coords[0], coords[1], coords[2], coords[3]
    for _ in range(3):
        print(f"{x1}, {y1}, {x2}, {y2}")
if __name__ == '__main__':
    shape_coords = [1, 1, 5, 5]
    print_shape_repeated(shape_coords)