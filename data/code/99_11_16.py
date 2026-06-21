def evaluate_nested_conditions(a, b, c, d, e):
    first_part = a and b
    if first_part:
        return True
    second_part = c and (d or e)
    return second_part

if __name__ == '__main__':
    a_val = True
    b_val = False
    c_val = True
    d_val = False
    e_val = True
    print(evaluate_nested_conditions(a_val, b_val, c_val, d_val, e_val))