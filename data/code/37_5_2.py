def calculate_areas(bases, heights):
    return [b * h for b, h in zip(bases, heights)]

if __name__ == '__main__':
    sample_bases = [10, 20, 30]
    sample_heights = [5, 7, 9]
    results = calculate_areas(sample_bases, sample_heights)
    for area in results:
        print(area)