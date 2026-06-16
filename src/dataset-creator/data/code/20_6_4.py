def filter_positive(data):
    return (x for x in data if x > 0)
if __name__ == '__main__':
    stream = [-5, -2, 3, 10, -8, 4]
    result = list(filter_positive(stream))
    print(result)