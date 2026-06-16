def filter_positive(numbers):
    return [num for num in numbers if num >= 0]
if __name__ == '__main__':
    data = [-5, -3, 0, 2, -10, 7, -4, 89]
    result = filter_positive(data)
    print(result)