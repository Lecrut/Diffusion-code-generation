def evaluate_conditions(a, b, c, d):
    result = (a > 0) and (b < 10) or (c == 5) and not d
    return result

if __name__ == '__main__':
    a_val = 5
    b_val = 8
    c_val = 5
    d_val = False
    print(evaluate_conditions(a_val, b_val, c_val, d_val))