def calculate_square_areas(side_lengths):
    areas = []
    for side in side_lengths:
        areas.append(side * side)
    return areas
if __name__ == '__main__':
    sample_sides = [2, 3, 5, 8]
    result_areas = calculate_square_areas(sample_sides)
    print(result_areas)