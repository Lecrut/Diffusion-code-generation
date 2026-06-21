def any_truthy(iterable):
    for value in iterable:
        if value:
            return True
    return False

if __name__ == '__main__':
    print(any_truthy([False, False, True]))
    print(any_truthy([False, False, False]))
    print(any_truthy([0, 0, 0]))
    print(any_truthy([1, 0, 0]))
    print(any_truthy([]))