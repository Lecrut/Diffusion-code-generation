def calculate_range(numbers):
    if not numbers:
        return 0.0
    min_value = min(numbers)
    max_value = max(numbers)
    return max_value - min_value

if __name__ == '__main__':
    sample_data = [10.5, 3.2, 8.8, 1.1, 5.0]
    result = calculate_range(sample_data)
    print(result)