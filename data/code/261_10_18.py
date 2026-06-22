def calculate_median(data):
    n = len(data)
    if n == 0:
        raise ValueError("Input list cannot be empty")
    sorted_data = sorted(data)
    return sorted_data[n // 2]

if __name__ == '__main__':
    sample_values = [7, 3, 9, 1, 5]
    print(calculate_median(sample_values))