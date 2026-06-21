def check_any_true(iterable):
    iterator = iter(iterable)
    try:
        while True:
            if next(iterator):
                return True
    except StopIteration:
        return False

if __name__ == '__main__':
    samples = [
        [False, False, True, False],
        [False, False, False],
        [True],
        [],
        [False, False, False, False],
        (True, False),
        (False, False)
    ]
    for i, sample in enumerate(samples):
        print(f"Sample {i}: {check_any_true(sample)}")