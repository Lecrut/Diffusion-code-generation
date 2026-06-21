def any_value_truthy(iterable):
    return any(iterable)

if __name__ == '__main__':
    print(any_value_truthy([0, 0, 0]))
    print(any_value_truthy([0, 1, 0]))
    print(any_value_truthy([]))
    print(any_value_truthy([None, False, 0]))
    print(any_value_truthy([None, False, 1]))