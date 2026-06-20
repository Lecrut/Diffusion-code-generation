def any_true(iterable):
    return any(iterable)

if __name__ == '__main__':
    print(any_true([False, False, True]))
    print(any_true([]))
    print(any_true(['', 0, None, [], {}, ()]))
    print(any_true(['hello', 42, [1], {'a': 1}, (2,)]))