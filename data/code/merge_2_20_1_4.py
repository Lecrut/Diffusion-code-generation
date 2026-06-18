def filter_positive(numbers):
    return [num for num in numbers if num >= 0]
if __name__ == '__main__':
    data = [-5, -1, 3, 7, -2, 89, 0]
    result = filter_positive(data)
    print(result)