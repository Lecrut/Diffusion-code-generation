def evaluate_nested_conditions(a, b, c, d, e):
    result = (a and b) or (c and not d) or e
    return result

if __name__ == '__main__':
    a_val = True
    b_val = False
    c_val = True
    d_val = True
    e_val = False
    output = evaluate_nested_conditions(a_val, b_val, c_val, d_val, e_val)
    print(output)