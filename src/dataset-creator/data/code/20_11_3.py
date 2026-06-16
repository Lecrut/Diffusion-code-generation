def filter_positive_numbers(collection):
    return [num for num in collection if isinstance(num, (int, float)) and num > 0]
if __name__ == '__main__':
    sample_data = [-5, 10, -3.5, 0, 2, 'hello', None, True]
    result = filter_positive_numbers(sample_data)
    print(result)