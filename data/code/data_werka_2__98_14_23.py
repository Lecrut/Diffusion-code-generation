def evaluate_conditions(a, b, c, d):
    result = (a > 0) and (b < 10) and (c == 5) and (d is not None)
    return result

if __name__ == '__main__':
    a_val = 10
    b_val = 5
    c_val = 5
    d_val = 1
    print(evaluate_conditions(a_val, b_val, c_val, d_val))