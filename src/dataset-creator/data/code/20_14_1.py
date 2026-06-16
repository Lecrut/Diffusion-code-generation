def filter_positive_numbers(numbers):
    return [num for num in numbers if num > 0]
if __name__ == '__main__':
    test_list = [-5, 10, -3, 0, 7, -2]
    result = filter_positive_numbers(test_list)
    print(result)