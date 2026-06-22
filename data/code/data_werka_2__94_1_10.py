def check_any_true(iterable):
    return any(iterable)

if __name__ == '__main__':
    samples = [
        [False, False, True, False],
        [False, False, False],
        [True],
        [],
        [False, False, False, False]
    ]
    for sample in samples:
        print(check_any_true(sample))