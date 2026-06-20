def check_any_true(bool_iterable):
    if not isinstance(bool_iterable, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    for element in bool_iterable:
        if not isinstance(element, bool):
            raise ValueError("All elements must be booleans")
        if element:
            return True
    return False

if __name__ == '__main__':
    sample1 = [False, False, False]
    sample2 = [True, False, False]
    sample3 = []
    sample4 = [True, True, True]
    print(f"Sample 1: {check_any_true(sample1)}")
    print(f"Sample 2: {check_any_true(sample2)}")
    print(f"Sample 3: {check_any_true(sample3)}")
    print(f"Sample 4: {check_any_true(sample4)}")