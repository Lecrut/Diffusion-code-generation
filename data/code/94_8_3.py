def any_true(iterable):
    return any(iterable)

if __name__ == '__main__':
    print(any_true([False, False, True]))
    print(any_true([0, 0, 0]))
    print(any_true(['', '', 'hello']))
    print(any_true([]))