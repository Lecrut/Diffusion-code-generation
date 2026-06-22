def calculate_median(data):
    if not data:
        return None

    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 1:
        median = sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        median = (mid1 + mid2) / 2

    return median

if __name__ == '__main__':
    samples = [
        [1, 5, 2, 8],
        [10, 20, 30, 40, 50],
        [7, 1, 4, 9, 2]
    ]

    for sample in samples:
        print(calculate_median(sample))