def calculate_range(numbers):
    if not isinstance(numbers, list) or not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("Input must be a list of numbers")
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_data = [10.5, 3.2, 99.8, -5.1, 42.0]
    try:
        range_value = calculate_range(sample_data)
        print(range_value)
    except ValueError as e:
        print(e)