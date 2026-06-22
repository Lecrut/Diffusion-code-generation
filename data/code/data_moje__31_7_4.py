def compute_square_areas(side_lengths):
    return [side ** 2 for side in side_lengths]

if __name__ == '__main__':
    sides = [3, 5, 7, 10]
    areas = compute_square_areas(sides)
    print(areas)