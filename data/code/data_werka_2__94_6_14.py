def check_any_true(bool_list):
    if not isinstance(bool_list, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    for item in bool_list:
        if not isinstance(item, bool):
            raise ValueError("All elements must be booleans")
    if len(bool_list) == 0:
        return False
    for val in bool_list:
        if val:
            return True
    return False

if __name__ == '__main__':
    sample_data = [False, False, False, True, False]
    result = check_any_true(sample_data)
    print(result)