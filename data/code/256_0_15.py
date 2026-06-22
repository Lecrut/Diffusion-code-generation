def calculate_range(numbers):
    if not numbers:
        return 0.0
    minimum = min(numbers)
    maximum = max(numbers)
    range_value = maximum - minimum
    return range_value

if __name__ == '__main__':
    sample_data = [12.3, 45.6, 78.9, 1.2, 34.5]
    result = calculate_range(sample_data)
    print(result)