def is_any_true(value, values):
    if not isinstance(value, bool):
        raise ValueError("value must be a boolean")
    if not isinstance(values, (list, tuple)):
        raise ValueError("values must be a list or tuple")
    for item in values:
        if not isinstance(item, bool):
            raise ValueError("all items in values must be booleans")
    lookup = {True: True, False: False}
    result = lookup.get(value, False)
    for v in values:
        if lookup.get(v, False):
            return True
    return result

if __name__ == '__main__':
    print(is_any_true(True, [False, False]))
    print(is_any_true(False, [False, True]))
    print(is_any_true(False, [False, False]))