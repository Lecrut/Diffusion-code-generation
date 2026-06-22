def first_true(seq):
    for val in seq:
        if val:
            yield True
            return
    yield False

if __name__ == '__main__':
    result = list(first_true([False, False, True, False]))
    print(result)