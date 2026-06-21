def evaluate_nested_logic(a, b, c, d):
    term_one = a and b
    term_two = c and not d
    return term_one or term_two

if __name__ == '__main__':
    val_a = True
    val_b = False
    val_c = True
    val_d = False
    output = evaluate_nested_logic(val_a, val_b, val_c, val_d)
    print(output)