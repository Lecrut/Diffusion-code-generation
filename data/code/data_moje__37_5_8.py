def calculate_parallelogram_areas(bases, heights):
    return [base * height for base, height in zip(bases, heights)]

if __name__ == '__main__':
    sample_bases = [5, 10, 7]
    sample_heights = [3, 4, 6]
    results = calculate_parallelogram_areas(sample_bases, sample_heights)
    for i, area in enumerate(results):
        print(f"Area {i+1}: {area}")