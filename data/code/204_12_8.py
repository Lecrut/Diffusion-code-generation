def find_median(numbers):
    if not numbers:
        raise ValueError("The input list cannot be empty.")
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (mid1 + mid2) / 2

if __name__ == '__main__':
    sample_input = [10, 5, 20, 15, 30]
    try:
        median_value = find_median(sample_input)
        print(median_value)
    except ValueError as e:
        print(e)