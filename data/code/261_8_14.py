def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n == 0:
        return None
    mid_index = n // 2
    if n % 2 == 1:
        median_value = sorted_data[mid_index]
    else:
        median_value = (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2
    return median_value

if __name__ == '__main__':
    samples = [
        [3, 1, 4, 1, 5, 9, 2, 6],
        [7, 8, 5, 3, 0, 9, 2],
        [1, 2, 3, 4, 5]
    ]
    for sample in samples:
        median_value = calculate_median(sample)
        print(median_value)