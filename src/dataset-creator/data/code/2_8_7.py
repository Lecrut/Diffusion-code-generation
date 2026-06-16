def filter_positive(numbers):
    return [num for num in numbers if num > 0]
if __name__ == '__main__':
    data = [-5, 3, -1, 0, 7, -2, 4]
    result = filter_positive(data)
    print(result)