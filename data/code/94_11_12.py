def check_any_true(values):
    if not isinstance(values, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    if len(values) == 0:
        return False
    for item in values:
        if item is True:
            return True
        if not isinstance(item, bool):
            raise ValueError("All elements must be boolean")
    return False

if __name__ == '__main__':
    sample_values = [False, False, True, False]
    result = check_any_true(sample_values)
    print(result)
    empty_values = []
    empty_result = check_any_true(empty_values)
    print(empty_result)
    mixed_values = [False, 1, False]
    try:
        check_any_true(mixed_values)
    except ValueError as e:
        print(e)