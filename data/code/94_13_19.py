def any_truthy(iterable):
    return any(item for item in iterable)

if __name__ == '__main__':
    print(any_truthy([0, False, None, '']))
    print(any_truthy(['hello', 42, True]))