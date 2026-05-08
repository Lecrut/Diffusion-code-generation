def check_complex_condition(a, b, c, d, x):
    result = (a > b) or (c == d) and (x > 10)
    return result
if __name__ == '__main__':
    val_a = 5
    val_b = 3
    val_c = 7
    val_d = 7
    val_x = 12
    final_outcome = check_complex_condition(val_a, val_b, val_c, val_d, val_x)
    print(final_outcome)