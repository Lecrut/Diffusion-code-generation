def check_any_true(iterable):
    if not hasattr(iterable, '__iter__'):
        raise ValueError("Input must be an iterable")
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
            if item:
                return True
        except StopIteration:
            return False
    return False

if __name__ == '__main__':
    sample_with_true = [False, False, True, False]
    sample_all_false = [False, False, False]
    sample_empty = []
    sample_single_true = [True]
    sample_single_false = [False]
    print(check_any_true(sample_with_true))
    print(check_any_true(sample_all_false))
    print(check_any_true(sample_empty))
    print(check_any_true(sample_single_true))
    print(check_any_true(sample_single_false))