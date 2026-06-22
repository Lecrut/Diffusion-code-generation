def calculate_areas(bases, heights):
    return [b * h for b, h in zip(bases, heights)]

if __name__ == '__main__':
    sample_bases = [5, 10, 15, 20]
    sample_heights = [3, 4, 5, 6]
    results = calculate_areas(sample_bases, sample_heights)
    for area in results:
        print(area)