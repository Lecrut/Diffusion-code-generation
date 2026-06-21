def any_true(iterable):
    for item in iterable:
        if item:
            return True
    return False

if __name__ == '__main__':
    print(any_true([False, False, True]))
    print(any_true([False, False, False]))
    print(any_true([]))
    print(any_true([0, 0, 0]))
    print(any_true([None, None, None]))