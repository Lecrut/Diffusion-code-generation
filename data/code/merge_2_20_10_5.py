def filter_positive(arr):
    return [x for x in arr if x >= 0]
if __name__ == '__main__':
    data = [-5, -1, 3, 7, -2, 8, 0]
    result = filter_positive(data)
    print(result)