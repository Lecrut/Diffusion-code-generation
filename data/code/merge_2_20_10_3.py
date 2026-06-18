def filter_positive(numbers):
    return [num for num in numbers if num >= 0]
if __name__ == '__main__':
    data = [-5, -10, 3, 7, -2, 0, 4]
    result = filter_positive(data)
    print(result)