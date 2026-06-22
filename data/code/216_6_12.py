def calculate_median(values):
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid_index = n // 2
    if n % 2 == 1:
        return float(sorted_values[mid_index])
    else:
        return (sorted_values[mid_index - 1] + sorted_values[mid_index]) / 2.0

if __name__ == '__main__':
    sample_values = [7.5, 3.1, 9.8, 4.6]
    median_value = calculate_median(sample_values)
    print(median_value)