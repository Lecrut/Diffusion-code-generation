def has_positive(iterable):
    return any(x > 0 for x in iterable)
if __name__ == '__main__':
    data = [1, -5, 3, 0, 2]
    print(has_positive(data))