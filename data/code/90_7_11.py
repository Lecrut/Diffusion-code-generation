def evaluate_boolean_logic(a, b, c, d):
    if not all(isinstance(x, bool) for x in [a, b, c, d]):
        raise ValueError("All inputs must be boolean values.")
    
    condition1 = (a and b) or (c and d)
    condition2 = (a or b) and (c or d)
    condition3 = a ^ b ^ c ^ d
    
    return condition1 or condition2 or condition3

if __name__ == '__main__':
    a_val = True
    b_val = False
    c_val = True
    d_val = False
    result = evaluate_boolean_logic(a_val, b_val, c_val, d_val)
    print(result)