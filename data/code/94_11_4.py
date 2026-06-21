def check_any_true(values):
    if not isinstance(values, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    if len(values) == 0:
        return False
    try:
        return any(values)
    except TypeError:
        raise ValueError("All elements must be boolean-like")

if __name__ == '__main__':
    test_data = [False, False, False]
    output = check_any_true(test_data)
    print(output)