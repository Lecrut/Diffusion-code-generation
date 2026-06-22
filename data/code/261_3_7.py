def find_median(sample):
    n = len(sample)
    if n == 0:
        return None
    sorted_sample = sorted(sample)
    mid = n // 2
    if n % 2 == 1:
        return sorted_sample[mid]
    else:
        return (sorted_sample[mid - 1] + sorted_sample[mid]) / 2.0

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_median(sample_data))