def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n == 0:
        return None
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
        [3, 1, 4, 1, 5, 9]
    ]
    for sample in samples:
        median_value = calculate_median(sample)
        print(f"Sample: {sample}")
        if median_value is not None:
            print(f"Median: {median_value}")
        else:
            print("Median: No data provided")
        print("-" * 20)