def find_median(numbers):
    if not numbers:
        return None
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid_index = n // 2
    if n % 2 == 1:
        return sorted_numbers[mid_index]
    else:
        return (sorted_numbers[mid_index - 1] + sorted_numbers[mid_index]) / 2.0

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    median_value = find_median(sample_values)
    print(f"The median value is: {median_value}")