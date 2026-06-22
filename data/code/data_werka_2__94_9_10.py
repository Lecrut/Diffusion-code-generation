def _validate_iterable(data):
    if data is None:
        raise ValueError("Input cannot be None")
    if not hasattr(data, '__iter__'):
        raise ValueError("Input must be an iterable")
    if isinstance(data, (str, bytes, bytearray)):
        raise ValueError("Input must be a sequence of booleans, not a string-like object")
    return data

def check_any_true(iterable):
    validated_data = _validate_iterable(iterable)
    try:
        iterator = iter(validated_data)
        while True:
            item = next(iterator)
            if item is True:
                return True
            if not isinstance(item, bool):
                if item:
                    return True
    except StopIteration:
        return False
    return False

if __name__ == '__main__':
    test_data_a = [False, False, True, False]
    test_data_b = [False, False, False]
    test_data_c = []
    test_data_d = [True]
    print(check_any_true(test_data_a))
    print(check_any_true(test_data_b))
    print(check_any_true(test_data_c))
    print(check_any_true(test_data_d))