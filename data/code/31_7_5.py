def compute_square_areas(sides):
    return [s * s for s in sides]

if __name__ == '__main__':
    side_lengths = [3, 4, 5, 6, 7]
    areas = compute_square_areas(side_lengths)
    print(areas)