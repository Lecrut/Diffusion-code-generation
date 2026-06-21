def check_both_false(a, b):
    if not (hasattr(a, '__bool__') or hasattr(a, '__len__') or isinstance(a, type(None))):
        raise ValueError(f"Unsupported type for a: {type(a)}")
    if not (hasattr(b, '__bool__') or hasattr(b, '__len__') or isinstance(b, type(None))):
        raise ValueError(f"Unsupported type for b: {type(b)}")
    return not (a or b)

if __name__ == '__main__':
    a = 0
    b = []
    result = check_both_false(a, b)
    print(result)