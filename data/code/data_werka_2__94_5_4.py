def has_early_true(values):
    status_map = {True: 'found', False: 'pending'}
    for val in values:
        if val:
            yield True
            return
    yield False

if __name__ == '__main__':
    sample_data = [False, False, False, True, False]
    result = list(has_early_true(sample_data))
    print(result)
    sample_data_empty = []
    result_empty = list(has_early_true(sample_data_empty))
    print(result_empty)
    sample_data_first = [True, False, False]
    result_first = list(has_early_true(sample_data_first))
    print(result_first)