def calculate_square_areas(side_lengths):
    areas = []
    for side in side_lengths:
        areas.append(side * side)
    return areas
if __name__ == '__main__':
    sample_sides = [3, 4, 5, 10]
    result = calculate_square_areas(sample_sides)
    print(result)