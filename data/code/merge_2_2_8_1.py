def filter_positive(numbers):
    return [num for num in numbers if num > 0]
if __name__ == '__main__':
    data = [-5, -2, 3, 0, 7, -10, 4.5]
    result = filter_positive(data)
    print(result)