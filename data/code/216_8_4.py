def calculate_median(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2]
    print(calculate_median(sample_values))