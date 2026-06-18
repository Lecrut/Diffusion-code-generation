def filter_positive_numbers(numbers):
    return [num for num in numbers if num > 0]
if __name__ == '__main__':
    data = [-5, 3, -12, 7, 0, 89, -4]
    result = filter_positive_numbers(data)
    print(result)