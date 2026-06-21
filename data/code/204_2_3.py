def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    median_value = calculate_median(sample_values)
    print(median_value)