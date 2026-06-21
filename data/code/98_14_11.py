def evaluate_conditions(a, b, c, d):
    result = (a > 0) and (b < 10) or (c == d)
    return bool(result)

if __name__ == '__main__':
    a_val = 5
    b_val = 3
    c_val = 10
    d_val = 10
    print(evaluate_conditions(a_val, b_val, c_val, d_val))