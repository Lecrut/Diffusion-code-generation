def evaluate_nested_logic(a, b, c, d):
    if not (isinstance(a, bool) and isinstance(b, bool) and isinstance(c, bool) and isinstance(d, bool)):
        raise ValueError("Arguments must be boolean")
    left_side = a and b
    right_side = c and (not d)
    return left_side or right_side

if __name__ == '__main__':
    val_a = True
    val_b = False
    val_c = True
    val_d = False
    output = evaluate_nested_logic(val_a, val_b, val_c, val_d)
    print(output)