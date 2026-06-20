def check_any_true(bool_iter):
    try:
        return any(bool_iter)
    except TypeError:
        raise ValueError("Input must be an iterable of booleans")

if __name__ == '__main__':
    sample1 = [False, False, False]
    sample2 = [True, False, False]
    sample3 = []
    sample4 = [True, True, True]
    print(f"Sample 1: {check_any_true(sample1)}")
    print(f"Sample 2: {check_any_true(sample2)}")
    print(f"Sample 3: {check_any_true(sample3)}")
    print(f"Sample 4: {check_any_true(sample4)}")