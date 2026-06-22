def first_true(seq):
    for val in seq:
        if val:
            yield True
            return
    yield False

if __name__ == '__main__':
    sample_data = [False, False, True, False]
    result = first_true(sample_data)
    print(next(result))