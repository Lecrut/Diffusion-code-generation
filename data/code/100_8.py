def check_complex_condition(a, b, c, d, x, y):
    result = (a > b) or (c == d) and (x * 2 > y)
    return result
if __name__ == '__main__':
    val_a = 10
    val_b = 5
    val_c = 7
    val_d = 7
    val_x = 3
    val_y = 10
    final_outcome = check_complex_condition(val_a, val_b, val_c, val_d, val_x, val_y)
    print(final_outcome)