def calculate_square_areas(side_lengths):
    return [side * side for side in side_lengths]

if __name__ == '__main__':
    sides = [2, 5, 8, 10, 15]
    areas = calculate_square_areas(sides)
    print(areas)