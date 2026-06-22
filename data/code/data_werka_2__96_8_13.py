def evaluate_expression(a, b, c, d):
    if not isinstance(a, bool):
        raise ValueError("a must be a boolean")
    if not isinstance(b, bool):
        raise ValueError("b must be a boolean")
    if not isinstance(c, bool):
        raise ValueError("c must be a boolean")
    if not isinstance(d, bool):
        raise ValueError("d must be a boolean")
    return (a and b) or (c and not d)

if __name__ == '__main__':
    result = evaluate_expression(True, False, True, False)
    print(result)