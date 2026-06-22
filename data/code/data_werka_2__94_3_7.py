def has_true_element(values):
    if not isinstance(values, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    for val in values:
        if not isinstance(val, bool):
            raise ValueError("All elements must be booleans")
    return any(values)

if __name__ == '__main__':
    sample_data = [False, False, True, False]
    result = has_true_element(sample_data)
    print(result)