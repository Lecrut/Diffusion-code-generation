def _validate_iterable(source):
    try:
        iter(source)
    except TypeError:
        raise ValueError("Input must be an iterable")
    return source

def check_any_true(iterable):
    validated = _validate_iterable(iterable)
    iterator = iter(validated)
    try:
        while True:
            value = next(iterator)
            if value:
                return True
    except StopIteration:
        return False

if __name__ == '__main__':
    data_with_true = [False, False, True, False]
    data_all_false = [False, False, False]
    data_empty = []
    data_single_true = [True]
    data_single_false = [False]
    print(check_any_true(data_with_true))
    print(check_any_true(data_all_false))
    print(check_any_true(data_empty))
    print(check_any_true(data_single_true))
    print(check_any_true(data_single_false))