def evaluate_expression(a, b, c, d):
    first_clause = a and b
    second_clause = c and not d
    return first_clause or second_clause

if __name__ == '__main__':
    val_a = False
    val_b = True
    val_c = True
    val_d = True
    output = evaluate_expression(val_a, val_b, val_c, val_d)
    print(output)