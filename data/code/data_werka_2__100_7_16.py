def evaluate_complex_logic(a, b, c, d):
    if not isinstance(a, bool):
        raise ValueError("a must be a boolean")
    if not isinstance(b, bool):
        raise ValueError("b must be a boolean")
    if not isinstance(c, bool):
        raise ValueError("c must be a boolean")
    if not isinstance(d, bool):
        raise ValueError("d must be a boolean")
    
    part1 = a and b
    part2 = c or d
    part3 = not (a and c)
    
    result = (part1 or part2) and part3
    return result

if __name__ == '__main__':
    a_val = True
    b_val = False
    c_val = True
    d_val = False
    
    outcome = evaluate_complex_logic(a_val, b_val, c_val, d_val)
    print(outcome)