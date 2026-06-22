def filter_greater_than_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 1:
        median = sorted_numbers[n // 2]
    else:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    
    return [num for num in numbers if num > median]

if __name__ == '__main__':
    sample_values = [3, 5, 1, 4, 2]
    result = filter_greater_than_median(sample_values)
    print(result)