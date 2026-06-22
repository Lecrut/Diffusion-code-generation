def has_true_element(values):
    if not isinstance(values, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    for item in values:
        if item is True:
            return True
    return False

if __name__ == '__main__':
    sample_list = [False, False, True, False]
    result = has_true_element(sample_list)
    print(result)