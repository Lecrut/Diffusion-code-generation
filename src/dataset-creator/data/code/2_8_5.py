def filter_positive_numbers(numbers):
    return [num for num in numbers if num > 0]
if __name__ == '__main__':
    data = [-5, -2, 3, 8, -1, 0.5, 7.2, -9]
    result = filter_positive_numbers(data)
    print(result)