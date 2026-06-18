def has_positive(iterable):
    return any(x > 0 for x in iterable)
if __name__ == '__main__':
    data = [1, -2, 3, -4]
    print(has_positive(data))