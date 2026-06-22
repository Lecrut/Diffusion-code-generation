def calculate_parallelogram_areas(base_height_pairs):
    return [base * height for base, height in base_height_pairs]

if __name__ == '__main__':
    sample_pairs = [(5, 3), (10, 4), (7, 6), (12, 2)]
    results = calculate_parallelogram_areas(sample_pairs)
    for i, area in enumerate(results):
        print(f"Pair {i + 1}: Area = {area}")