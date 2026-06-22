def find_median(sample):
    n = len(sample)
    if n == 0:
        raise ValueError("Sample must not be empty")
    sorted_sample = sorted(sample)
    mid = n // 2
    return (sorted_sample[mid] + sorted_sample[~mid]) / 2.0

if __name__ == '__main__':
    sample_values = [1, 3, 5]
    try:
        median = find_median(sample_values)
        print(median)
    except ValueError as e:
        print(e)