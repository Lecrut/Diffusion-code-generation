def compute_square_areas(side_lengths):
    return [side ** 2 for side in side_lengths]

if __name__ == '__main__':
    sides = [2, 4, 6, 8, 10]
    areas = compute_square_areas(sides)
    print(areas)