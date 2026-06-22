def get_middle_value(numbers):
    if not numbers:
        return None
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2

if __name__ == '__main__':
    sample_array = [3, 1, 4, 1, 5, 9, 2]
    result = get_middle_value(sample_array)
    print(result)