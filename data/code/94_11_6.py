def check_any_true(values):
    if not isinstance(values, (list, tuple)):
        raise ValueError("Input must be a sequence")
    for item in values:
        if item is not True and item is not False:
            raise ValueError("All elements must be boolean")
    return True if values and any(values) else False

if __name__ == '__main__':
    sample_data = [False, True, False]
    result = check_any_true(sample_data)
    print(result)