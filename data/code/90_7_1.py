def check_complex_conditions(a, b, c, d, e):
    condition1 = (a & b) | (c & d)
    condition2 = (a | b) & (c | d)
    condition3 = (a ^ b) | (c ^ d)
    result = condition1 | condition2 | condition3
    return result
if __name__ == '__main__':
    a_val = 5
    b_val = 3
    c_val = 6
    d_val = 1
    e_val = 7
    result = check_complex_conditions(a_val, b_val, c_val, d_val, e_val)
    print(result)