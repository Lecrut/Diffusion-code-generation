def filter_non_negative(data):
    return (x for x in data if x >= 0)
if __name__ == '__main__':
    stream = [-5, -1, 0, 3, 7, -2, 8]
    result = list(filter_non_negative(stream))
    print(result)