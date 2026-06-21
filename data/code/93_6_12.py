def check_both_false(a, b):
    if not hasattr(a, '__bool__') and not isinstance(a, type(None)):
        raise ValueError("a does not support boolean evaluation")
    if not hasattr(b, '__bool__') and not isinstance(b, type(None)):
        raise ValueError("b does not support boolean evaluation")
    return not bool(a) and not bool(b)

if __name__ == '__main__':
    a = 0
    b = []
    result = check_both_false(a, b)
    print(result)