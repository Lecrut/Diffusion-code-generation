def filter_positive_numbers(numbers):
    return [num for num in numbers if num >= 0]
if __name__ == '__main__':
    data = [-5, -2, 3, 7, -10, 4, -8, 9, 0, -3]
    result = filter_positive_numbers(data)
    print(result)