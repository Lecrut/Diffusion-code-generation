def any_truthy(iterable):
    return any(item for item in iterable)

if __name__ == '__main__':
    print(any_truthy([0, '', None, False]))
    print(any_truthy(['hello', 1, True]))