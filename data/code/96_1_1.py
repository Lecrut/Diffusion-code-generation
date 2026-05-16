def evaluate_nested_logic(a, b, c, d):
    result = (a and b) or (c and not d)
    return result
if __name__ == '__main__':
    a_val = True
    b_val = False
    c_val = True
    d_val = False
    output = evaluate_nested_logic(a_val, b_val, c_val, d_val)
    print(output)