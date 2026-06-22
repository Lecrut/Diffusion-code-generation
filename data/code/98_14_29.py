def evaluate_conditions(a, b, c, d):
    result = (a > 0) and (b < 10) or (c == d)
    return bool(result)

if __name__ == '__main__':
    val_a = 5
    val_b = 8
    val_c = 3
    val_d = 3
    print(evaluate_conditions(val_a, val_b, val_c, val_d))