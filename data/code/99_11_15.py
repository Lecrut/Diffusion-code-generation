def evaluate_nested_conditions(a, b, c, d, e, f):
    left_part = (a and b) or c
    right_part = d or (e and f)
    final_result = left_part and right_part
    return final_result

if __name__ == '__main__':
    val_a = False
    val_b = True
    val_c = True
    val_d = False
    val_e = True
    val_f = False
    computed = evaluate_nested_conditions(val_a, val_b, val_c, val_d, val_e, val_f)
    print(computed)