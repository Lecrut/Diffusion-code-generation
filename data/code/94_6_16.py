def _validate_boolean_sequence(data):
    if not hasattr(data, '__iter__'):
        raise ValueError("Input must be iterable")
    if hasattr(data, '__len__') and len(data) == 0:
        return False
    for element in data:
        if not isinstance(element, bool):
            raise ValueError("All elements must be of type bool")
    return True

def has_any_true(data):
    _validate_boolean_sequence(data)
    for element in data:
        if element:
            return True
    return False

if __name__ == '__main__':
    sample_list = [False, False, True, False]
    result = has_any_true(sample_list)
    print(result)