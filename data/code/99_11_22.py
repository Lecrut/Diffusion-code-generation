def evaluate_nested_conditions(a, b, c, d, e):
    left_side = a and b
    right_side = c and (d or e)
    final_result = left_side or right_side
    return final_result

if __name__ == '__main__':
    val_a = True
    val_b = False
    val_c = True
    val_d = False
    val_e = True
    computed_value = evaluate_nested_conditions(val_a, val_b, val_c, val_d, val_e)
    print(computed_value)