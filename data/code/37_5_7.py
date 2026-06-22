def calculate_areas(bases, heights):
    return [b * h for b, h in zip(bases, heights)]

if __name__ == '__main__':
    sample_bases = [10, 5, 8, 15]
    sample_heights = [4, 7, 3, 6]
    results = calculate_areas(sample_bases, sample_heights)
    for result in results:
        print(result)