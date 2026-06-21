def evaluate_nested_logic(a, b, c, d):
    if not all(isinstance(x, bool) for x in (a, b, c, d)):
        raise ValueError("All arguments must be boolean")
    
    left_side = a and b
    right_side = c and (not d)
    
    return left_side or right_side

if __name__ == '__main__':
    val_a = True
    val_b = False
    val_c = True
    val_d = False
    calculated_result = evaluate_nested_logic(val_a, val_b, val_c, val_d)
    print(calculated_result)