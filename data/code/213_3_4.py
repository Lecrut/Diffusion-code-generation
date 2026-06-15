def calculate_stats(data):
    if not data:
        return None, None, None
    sorted_data = sorted(data)
    n = len(sorted_data)
    mean = sum(sorted_data) / n
    if n % 2 == 1:
        median = sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        median = (mid1 + mid2) / 2
    range_val = sorted_data[-1] - sorted_data[0]
    return mean, median, range_val
if __name__ == '__main__':
    sample_data = [10.5, 22.333333333333332, 4.1, 15.0, 8.9]
    mean_val, median_val, range_val = calculate_stats(sample_data)
    print(f"Data: {sample_data}")
    print(f"Arithmetic Mean: {mean_val}")
    print(f"Median: {median_val}")
    print(f"Range: {range_val}")