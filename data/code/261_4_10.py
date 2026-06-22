def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n == 0:
        return None
    elif n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (mid1 + mid2) / 2

if __name__ == '__main__':
    sample_values = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    median_value = calculate_median(sample_values)
    print(median_value)