def filter_positive(arr):
    return [x for x in arr if x >= 0]
if __name__ == '__main__':
    data = [-5, 10, -3, 7, -2, 4]
    result = filter_positive(data)
    print(result)