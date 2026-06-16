def filter_positive_numbers(numbers):
    return [num for num in numbers if isinstance(num, (int, float)) and num > 0]
if __name__ == '__main__':
    sample_data = [-5, -2, 3, 0, 7.5, 'a', None, True]
    result = filter_positive_numbers(sample_data)
    print(result)