def find_median(samples):
    sorted_samples = sorted(samples)
    n = len(sorted_samples)
    if n == 0:
        return None
    elif n % 2 == 1:
        return sorted_samples[n // 2]
    else:
        mid1 = sorted_samples[n // 2 - 1]
        mid2 = sorted_samples[n // 2]
        return (mid1 + mid2) / 2
if __name__ == '__main__':
    sample1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sample2 = [10, 22, -1, 5, 7, 8, 9, 1, 5, 3, 0, 4, 2]
    sample3 = []
    print(find_median(sample1))
    print(find_median(sample2))
    print(find_median(sample3))