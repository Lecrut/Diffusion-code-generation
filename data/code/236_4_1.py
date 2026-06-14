def print_shape_repeated(coords):
    x1, y1, x2, y2 = coords
    shape = f"({x1}, {y1}) to ({x2}, {y2})"
    for _ in range(3):
        print(shape)
if __name__ == '__main__':
    sample_coords = [0, 0, 5, 10]
    print_shape_repeated(sample_coords)