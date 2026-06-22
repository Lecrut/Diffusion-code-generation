def evaluate_nested_logic(a, b, c, d):
    if not all(isinstance(arg, bool) for arg in (a, b, c, d)):
        raise ValueError("All arguments must be boolean types")
    term_one = a and b
    term_two = c and (not d)
    return term_one or term_two

if __name__ == '__main__':
    a_val = True
    b_val = False
    c_val = True
    d_val = False
    result = evaluate_nested_logic(a_val, b_val, c_val, d_val)
    print(result)