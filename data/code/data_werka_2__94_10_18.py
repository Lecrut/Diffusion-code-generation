def is_any_true(flag, items):
    if not isinstance(flag, bool):
        raise ValueError("flag must be a boolean")
    if not isinstance(items, (list, tuple)):
        raise ValueError("items must be a list or tuple")
    if flag:
        return True
    if any(items):
        return True
    return False

if __name__ == '__main__':
    print(is_any_true(True, [False, False]))
    print(is_any_true(False, [False, True]))
    print(is_any_true(False, [False, False]))
    print(is_any_true(False, []))