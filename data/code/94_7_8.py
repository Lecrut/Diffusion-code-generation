def any_truthy(iterable):
    for item in iterable:
        if item:
            return True
    return False

if __name__ == '__main__':
    print(any_truthy([False, False, True]))
    print(any_truthy([False, False, False]))
    print(any_truthy([]))
    print(any_truthy([0, 0, 0]))
    print(any_truthy([None, None, None]))