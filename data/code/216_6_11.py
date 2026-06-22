def calculate_median(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2.0
    else:
        return float(sorted_numbers[mid])

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, 2.9, 5.1]
    print(calculate_median(sample_values))