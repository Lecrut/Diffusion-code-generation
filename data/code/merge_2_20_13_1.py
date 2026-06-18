def filter_positive(iterable):
    return (x for x in iterable if x > 0)
if __name__ == '__main__':
    data = [1, -5, 3, 0, 2, -9]
    result = list(filter_positive(data))
    print(result)