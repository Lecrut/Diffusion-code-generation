def contains_true(values):
    if not isinstance(values, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    for item in values:
        if item is True:
            return True
    return False

if __name__ == '__main__':
    sample_data = [False, False, True, False]
    output = contains_true(sample_data)
    print(output)