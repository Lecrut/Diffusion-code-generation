def evaluate_nested_logic(a, b, c, d):
    term_left = a and b
    term_right = c and (not d)
    return term_left or term_right

if __name__ == '__main__':
    val_a = False
    val_b = True
    val_c = True
    val_d = True
    output = evaluate_nested_logic(val_a, val_b, val_c, val_d)
    print(output)