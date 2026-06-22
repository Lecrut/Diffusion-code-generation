def calculate_difference(numbers):
    if not numbers:
        return 0
    min_value = min(numbers)
    max_value = max(numbers)
    return max_value - min_value

if __name__ == '__main__':
    sample_numbers = [10, 3, 7, 2, 9]
    result = calculate_difference(sample_numbers)
    print(result)