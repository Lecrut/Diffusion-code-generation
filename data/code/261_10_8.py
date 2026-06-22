def calculate_median(data):
    n = len(data)
    if n == 0:
        raise ValueError("Input list cannot be empty")
    sorted_data = sorted(data)
    index = n // 2
    return sorted_data[index] if n % 2 != 0 else (sorted_data[index - 1] + sorted_data[index]) / 2

if __name__ == '__main__':
    sample_values = [7, 2, 5, 3, 8]
    median_value = calculate_median(sample_values)
    print(median_value)