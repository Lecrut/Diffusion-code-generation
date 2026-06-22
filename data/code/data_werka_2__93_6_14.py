def check_both_false(a, b):
    if not hasattr(a, '__bool__'):
        raise ValueError("a must be a boolean-like type")
    if not hasattr(b, '__bool__'):
        raise ValueError("b must be a boolean-like type")
    return not bool(a) and not bool(b)

if __name__ == '__main__':
    a = 0
    b = []
    result = check_both_false(a, b)
    print(result)