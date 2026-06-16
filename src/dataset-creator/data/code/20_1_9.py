def filter_positive(numbers):
    return [x for x in numbers if x >= 0]
if __name__ == '__main__':
    data = [-5, -2, 3, 10, -7, 4, -9, 8]
    result = filter_positive(data)
    print(result)