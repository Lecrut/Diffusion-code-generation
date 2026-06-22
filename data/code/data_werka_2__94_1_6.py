def _validate_iterable(obj):
    if not hasattr(obj, '__iter__'):
        raise ValueError("Input must be an iterable")
    return obj

def check_any_true(iterable):
    _validate_iterable(iterable)
    return any(iterable)

if __name__ == '__main__':
    data_sets = [
        [False, False, True, False],
        [False, False, False],
        [True],
        [],
        [False, False, False, False]
    ]
    for idx, sample in enumerate(data_sets):
        result = check_any_true(sample)
        print(f"result_{idx}: {result}")