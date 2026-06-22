def calculate_parallelogram_areas(bases, heights):
    return [b * h for b, h in zip(bases, heights)]

if __name__ == '__main__':
    sample_bases = [10, 15, 20]
    sample_heights = [5, 8, 3]
    areas = calculate_parallelogram_areas(sample_bases, sample_heights)
    for area in areas:
        print(area)