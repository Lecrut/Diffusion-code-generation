def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def filter_greater_than_median(numbers):
    if not numbers:
        return []
    median = calculate_median(numbers)
    return [num for num in numbers if num > median]

if __name__ == '__main__':
    sample_values = [7, 3, 8, 2, 5, 6, 1, 4]
    result = filter_greater_than_median(sample_values)
    print(result)