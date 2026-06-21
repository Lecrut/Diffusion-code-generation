def find_median(numbers):
    if not numbers:
        return None
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 1:
        return sorted_numbers[mid]
    else:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2.0

if __name__ == '__main__':
    sample_input = [10, 5, 20, 15, 30]
    median_value = find_median(sample_input)
    print(median_value)