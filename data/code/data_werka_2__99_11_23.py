def evaluate_nested_conditions(a, b, c, d):
    result = (a and b) or (c and d)
    return result

if __name__ == '__main__':
    a_val = True
    b_val = False
    c_val = True
    d_val = True
    print(evaluate_nested_conditions(a_val, b_val, c_val, d_val))