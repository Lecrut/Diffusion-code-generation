def any_true(seq):
    for val in seq:
        if val:
            return True
    return False

if __name__ == '__main__':
    print(any_true([False, False, True, False]))
    print(any_true([False, False, False]))
    print(any_true([True]))