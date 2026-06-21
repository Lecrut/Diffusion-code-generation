def _validate_boolean_sequence(data):
    if not hasattr(data, '__iter__'):
        raise ValueError("Input must be iterable")
    for index, element in enumerate(data):
        if not isinstance(element, bool):
            raise ValueError(f"Element at index {index} is not a boolean")
    return list(data)

def check_any_true(data):
    validated_data = _validate_boolean_sequence(data)
    for item in validated_data:
        if item is True:
            return True
    return False

if __name__ == '__main__':
    sample_list = [False, False, True, False]
    result = check_any_true(sample_list)
    print(result)