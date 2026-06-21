def evaluate_nested_conditions(a, b, c, d, e):
    left_side = a and b
    right_side_part = d or e
    right_side = c and right_side_part
    final_result = left_side or right_side
    return final_result

if __name__ == '__main__':
    val_a = False
    val_b = True
    val_c = False
    val_d = True
    val_e = False
    computed_value = evaluate_nested_conditions(val_a, val_b, val_c, val_d, val_e)
    print(computed_value)