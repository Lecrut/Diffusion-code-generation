def check_complex_conditions(a, b, c, d):
    condition1 = (a & b) | (c & d)
    condition2 = (a | b) & (c | d)
    condition3 = a ^ b ^ c ^ d
    return condition1 or condition2 or condition3
if __name__ == '__main__':
    a_val = 1
    b_val = 2
    c_val = 3
    d_val = 4
    result = check_complex_conditions(a_val, b_val, c_val, d_val)
    print(result)