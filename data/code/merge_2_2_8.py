def filter_positive_numbers(numbers):
    return [num for num in numbers if num > 0]
if __name__ == '__main__':
    data = [-5, 3, -12, 0, 8, -7.5, 4.2, 9]
    result = filter_positive_numbers(data)
    print(result)