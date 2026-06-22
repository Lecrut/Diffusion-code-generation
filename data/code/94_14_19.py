def has_true_element(values):
    if not hasattr(values, '__iter__') or isinstance(values, str):
        raise ValueError("Input must be an iterable of booleans")
    def is_boolean(item):
        return isinstance(item, bool)
    if any(not is_boolean(item) for item in values):
        raise ValueError("All elements must be boolean values")
    for item in values:
        if item is True:
            return True
    return False

if __name__ == '__main__':
    sample_list = [True, False, False, True]
    result = has_true_element(sample_list)
    print(result)