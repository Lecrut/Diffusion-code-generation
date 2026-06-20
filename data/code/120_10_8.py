def identity_and_type_safe_equal(a, b):
    if type(a) is not type(b):
        return False
    if a is b:
        return True
    try:
        return a == b
    except Exception:
        return False
if __name__ == '__main__':
    value1 = [1, 2, 3]
    value2 = [1, 2, 3]
    value3 = (1, 2, 3)
    print(identity_and_type_safe_equal(value1, value2))
    print(identity_and_type_safe_equal(value1, value3))