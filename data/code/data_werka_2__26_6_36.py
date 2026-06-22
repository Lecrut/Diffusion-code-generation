def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        median = sorted_numbers[mid]
    return median

def filter_greater_than_median(numbers):
    if not numbers:
        return []
    median_value = calculate_median(numbers)
    return [num for num in numbers if num > median_value]

if __name__ == '__main__':
    sample_values = [7, 3, 8, 1, 2, 9, 4, 6, 5]
    result = filter_greater_than_median(sample_values)
    print(result)