def filter_positive(numbers):
    return [x for x in numbers if x >= 0]
if __name__ == '__main__':
    data = [-5, -2, 3, -10, 7, 0, -8, 4]
    result = filter_positive(data)
    print(result)