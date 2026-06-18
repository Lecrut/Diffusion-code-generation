def filter_positive(numbers):
    return [x for x in numbers if x > 0]
if __name__ == '__main__':
    data = [-5, -1, 3, 7, -2, 9, 0, 4, -8]
    result = filter_positive(data)
    print(result)