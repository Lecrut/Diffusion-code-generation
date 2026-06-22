def calculate_range(numbers):
    if not numbers:
        return 0.0
    min_value = min(numbers)
    max_value = max(numbers)
    return max_value - min_value

if __name__ == '__main__':
    sample_data = [12.3, 45.6, 78.9, 1.2, 3.4]
    result = calculate_range(sample_data)
    print(result)