def calculate_parallelogram_areas(base_height_pairs):
    return [base * height for base, height in base_height_pairs]

if __name__ == '__main__':
    pairs = [(10, 5), (12, 4), (7, 9)]
    areas = calculate_parallelogram_areas(pairs)
    print(areas)