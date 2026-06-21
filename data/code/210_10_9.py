def calculate_range(numbers):
    if not numbers:
        return 0
    min_value = min(numbers)
    max_value = max(numbers)
    range_value = max_value - min_value
    return range_value

if __name__ == '__main__':
    sample_values = [15, 22, 36, 4, 89]
    result = calculate_range(sample_values)
    print(result)