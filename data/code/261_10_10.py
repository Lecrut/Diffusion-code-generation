def calculate_median(data):
    n = len(data)
    if n == 0:
        raise ValueError("Input list cannot be empty")
    sorted_data = sorted(data)
    median_index = n // 2
    return sorted_data[median_index]

if __name__ == '__main__':
    sample_values = [10, 5, 8, 12, 3, 9, 6]
    try:
        print(calculate_median(sample_values))
    except ValueError as e:
        print(e)