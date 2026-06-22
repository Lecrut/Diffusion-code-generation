def calculate_median(data):
    n = len(data)
    sorted_data = sorted(data)
    middle_index = n // 2
    if n % 2 == 0:
        return (sorted_data[middle_index - 1] + sorted_data[middle_index]) / 2
    else:
        return sorted_data[middle_index]

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    median_value = calculate_median(sample_values)
    print(median_value)