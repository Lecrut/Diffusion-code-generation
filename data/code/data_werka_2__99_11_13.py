def evaluate_nested_conditions(a, b, c, d, e):
    if not isinstance(a, bool):
        raise ValueError("a must be a boolean")
    if not isinstance(b, bool):
        raise ValueError("b must be a boolean")
    if not isinstance(c, bool):
        raise ValueError("c must be a boolean")
    if not isinstance(d, bool):
        raise ValueError("d must be a boolean")
    if not isinstance(e, bool):
        raise ValueError("e must be a boolean")
    
    left_part = a and b
    right_part = c and (d or e)
    result = left_part or right_part
    return result

if __name__ == '__main__':
    val_a = False
    val_b = True
    val_c = True
    val_d = False
    val_e = False
    final_result = evaluate_nested_conditions(val_a, val_b, val_c, val_d, val_e)
    print(final_result)