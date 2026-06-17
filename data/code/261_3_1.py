def calculate_multiple_medians(data):
    medians = []
    for sample in data:
        sorted_sample = sorted(sample)
        n = len(sorted_sample)
        if n == 0:
            median = None
        elif n % 2 == 1:
            median = sorted_sample[n // 2]
        else:
            mid1 = sorted_sample[n // 2 - 1]
            mid2 = sorted_sample[n // 2]
            median = (mid1 + mid2) / 2
        medians.append(median)
    return medians
if __name__ == '__main__':
    samples = [
        [1, 3, 5],
        [2, 4, 6, 8],
        [10, 20, 30, 40, 50],
        [],
        [7]
    ]
    result = calculate_multiple_medians(samples)
    print(result)