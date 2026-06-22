def compute_square_areas(side_lengths):
    return [side ** 2 for side in side_lengths]

if __name__ == '__main__':
    hard_coded_sides = [1, 2, 3, 4, 5]
    areas = compute_square_areas(hard_coded_sides)
    print(areas)