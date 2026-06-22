def filter_greater_than_median(numbers):
    if not numbers:
        return []
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    
    if n % 2 == 0:
        median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        median = sorted_numbers[mid]
    
    return [num for num in numbers if num > median]

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = filter_greater_than_median(sample_values)
    print(result)