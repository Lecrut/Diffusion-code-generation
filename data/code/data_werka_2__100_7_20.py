def evaluate_complex_condition(a: bool, b: bool, c: bool, d: bool) -> bool:
    term1 = a and b
    term2 = not c and d
    term3 = a and (not b) and c
    result = term1 or term2 or term3
    return result
if __name__ == '__main__':
    a_val = True
    b_val = False
    c_val = True
    d_val = True
    outcome = evaluate_complex_condition(a_val, b_val, c_val, d_val)
    print(outcome)