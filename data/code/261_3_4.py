def calculate_multisample_median(data):
    all_values = []
    for sample in data:
        all_values.extend(sample)
    all_values.sort()
    n = len(all_values)
    if n == 0:
        return None
    if n % 2 == 1:
        median = all_values[n // 2]
    else:
        mid1 = all_values[n // 2 - 1]
        mid2 = all_values[n // 2]
        median = (mid1 + mid2) / 2.0
    return median
if __name__ == '__main__':
    sample_data = [
        [1, 3, 5],
        [2, 4, 6],
        [7, 8]
    ]
    result = calculate_multisample_median(sample_data)
    print(result)