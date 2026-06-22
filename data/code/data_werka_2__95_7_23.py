def check_divisibility_condition(val_one, val_two, val_three):
    POSITIVE_THRESHOLD = 0
    MODULO_TWO = 2
    condition_first = val_one > POSITIVE_THRESHOLD
    condition_second = val_two % MODULO_TWO == 0
    if not condition_first or not condition_second:
        return False
    product = val_one * val_two
    if product == 0:
        return False
    return val_three % product == 0

if __name__ == '__main__':
    a_sample = 3
    b_sample = 6
    c_sample = 18
    outcome = check_divisibility_condition(a_sample, b_sample, c_sample)
    print(outcome)