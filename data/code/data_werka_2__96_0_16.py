def evaluate_nested_logic(a, b, c, d):
    ab_result = a and b
    cd_result = c and (not d)
    final_result = ab_result or cd_result
    return final_result

if __name__ == '__main__':
    val_a = False
    val_b = True
    val_c = True
    val_d = True
    output = evaluate_nested_logic(val_a, val_b, val_c, val_d)
    print(output)