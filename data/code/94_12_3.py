def has_truthy(iterable):
    return any(iterable)

if __name__ == '__main__':
    print(has_truthy([0, 0, 0]))
    print(has_truthy([0, 1, 0]))
    print(has_truthy([]))
    print(has_truthy([None, False, 0]))
    print(has_truthy([None, False, 1]))