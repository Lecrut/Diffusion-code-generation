def calculate_range(numbers):
    if not numbers:
        return 0
    min_value = min(numbers)
    max_value = max(numbers)
    return max_value - min_value

if __name__ == '__main__':
    sample_values = [15, 27, 9, 36, 42]
    result = calculate_range(sample_values)
    print(result)