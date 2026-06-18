def filter_positive(data):
    return (x for x in data if x > 0)
if __name__ == '__main__':
    stream = [10, -5, 3.7, -2.1, 8]
    result = list(filter_positive(stream))
    print(result)