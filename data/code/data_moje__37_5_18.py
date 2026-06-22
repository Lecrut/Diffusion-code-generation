def calculate_parallelogram_areas(bases_heights):
    return [base * height for base, height in bases_heights]

if __name__ == '__main__':
    sample_pairs = [(10, 5), (7, 3), (12, 8), (4, 6)]
    areas = calculate_parallelogram_areas(sample_pairs)
    for i, area in enumerate(areas):
        print(f"Pair {i+1}: {area}")