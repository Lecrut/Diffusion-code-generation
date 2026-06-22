TRUE_VALUE = 1
FALSE_VALUE = 0

def check_any_true(iterable):
    accumulator = FALSE_VALUE
    for element in iterable:
        if element:
            accumulator = TRUE_VALUE
            break
    return bool(accumulator)

if __name__ == '__main__':
    data_sets = [
        [False, False, False],
        [True, False, False],
        [False, True, False],
        [False, False, True],
        [True, True, True],
        [],
        [0, 0, 1],
        [1, 0, 0]
    ]
    for dataset in data_sets:
        result = check_any_true(dataset)
        print(result)