def check_complex_condition(a, b, c, d, x, y):
    result = (a > b) or (c == d) and (x + y > 10)
    return result
if __name__ == '__main__':
    val_a = 10
    val_b = 5
    val_c = 8
    val_d = 8
    val_x = 3
    val_y = 4
    final_outcome = check_complex_condition(val_a, val_b, val_c, val_d, val_x, val_y)
    print(final_outcome)