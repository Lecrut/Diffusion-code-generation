def evaluate_nested_logic(a, b, c, d):
    if not isinstance(a, bool) or not isinstance(b, bool) or not isinstance(c, bool) or not isinstance(d, bool):
        raise ValueError("All arguments must be boolean.")
    return (a and b) or (c and not d)

if __name__ == '__main__':
    A = True
    B = False
    C = True
    D = False
    result = evaluate_nested_logic(A, B, C, D)
    print(result)