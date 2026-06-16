def filter_positive(arr):
    return [x for x in arr if x >= 0]
if __name__ == '__main__':
    data = [-5, -2, 3, 7, -10, 0, 4]
    result = filter_positive(data)
    print(result)