def filter_positive_numbers(numbers):
    return [num for num in numbers if num > 0]
if __name__ == '__main__':
    sample_data = [-5, -3, 0, 2, 4, 10.5, -7, 8]
    result = filter_positive_numbers(sample_data)
    print(result)