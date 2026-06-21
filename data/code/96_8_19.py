def evaluate_expression(a, b, c, d):
    first_part = a and b
    second_part = c and (not d)
    return first_part or second_part

if __name__ == '__main__':
    val_a = False
    val_b = True
    val_c = True
    val_d = True
    result = evaluate_expression(val_a, val_b, val_c, val_d)
    print(result)