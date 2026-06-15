def print_shape_repeated(coords):
    x1, y1, x2, y2 = coords
    for _ in range(3):
        print(f"{x1}, {y1}, {x2}, {y2}")
if __name__ == '__main__':
    sample_coords = (0, 0, 4, 2)
    print_shape_repeated(sample_coords)