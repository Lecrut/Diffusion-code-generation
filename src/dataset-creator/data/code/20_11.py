def filter_positive_numbers(numbers):
    return [num for num in numbers if isinstance(num, (int, float)) and num > 0]
if __name__ == '__main__':
    sample_data = [-5, 10, -3.7, 0, '2', True, None, 42]
    result = filter_positive_numbers(sample_data)
    print(result)