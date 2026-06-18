def filter_positive_numbers(numbers):
    return [num for num in numbers if num >= 0]
if __name__ == '__main__':
    data = [-5, -10, 3, 7, -2, 0, 4, -8, 9]
    result = filter_positive_numbers(data)
    print(result)