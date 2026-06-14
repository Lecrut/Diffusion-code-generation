def print_shape_repeated(coords):
    x1, y1, x2, y2 = coords
    points = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
    for _ in range(3):
        for x, y in points:
            print(f"{x} {y}")
if __name__ == '__main__':
    sample_coords = [0, 0, 4, 2]
    print_shape_repeated(sample_coords)