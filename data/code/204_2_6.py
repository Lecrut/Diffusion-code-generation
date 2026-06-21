def calculate_median(numbers):
    n = len(numbers)
    if n == 0:
        raise ValueError("Input list cannot be empty")
    sorted_numbers = sorted(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2.0
    else:
        return sorted_numbers[mid]

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    median_value = calculate_median(sample_values)
    print(median_value)