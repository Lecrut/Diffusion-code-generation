def evaluate_expression(a, b, c, d):
    if not all(isinstance(x, bool) for x in (a, b, c, d)):
        raise ValueError("Inputs must be boolean")
    return bool((a and b) or (c and not d))

if __name__ == '__main__':
    result = evaluate_expression(True, False, True, False)
    print(result)