def check_any_true(iterable):
    if not isinstance(iterable, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    
    return any(iterable)

if __name__ == '__main__':
    print(f"check_any_true([False, False, True]): {check_any_true([False, False, True])}")
    print(f"check_any_true((False, False, False)): {check_any_true((False, False, False))}")
    print(f"check_any_true([True, False, False]): {check_any_true([True, False, False])}")