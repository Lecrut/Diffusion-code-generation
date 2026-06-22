def check_conditions(val_a: float, val_b: float, val_c: float) -> bool:
    first_positive = val_a > 0.0
    second_smaller = val_b < val_a
    sum_match = val_c == (val_a + val_b)
    return first_positive and second_smaller and sum_match

if __name__ == '__main__':
    a_val = 15.5
    b_val = 10.2
    c_val = 25.7
    outcome = check_conditions(a_val, b_val, c_val)
    print(outcome)