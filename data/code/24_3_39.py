def filter_negative_numbers(numbers):
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list")
    return [num for num in numbers if isinstance(num, int) and num < 0]

if __name__ == '__main__':
    sample_values = [10, -3, 7, -8, 0, -5, 2]
    negative_numbers = filter_negative_numbers(sample_values)
    print(negative_numbers)