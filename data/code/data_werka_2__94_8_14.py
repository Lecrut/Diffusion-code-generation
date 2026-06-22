def check_truth_presence(values):
    if not isinstance(values, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    if len(values) == 0:
        return False
    for value in values:
        if value is True:
            return True
    return False

if __name__ == '__main__':
    test_data = [False, False, True, False]
    result = check_truth_presence(test_data)
    print(result)