def are_both_variables_false(val_a: bool, val_b: bool) -> bool:
    condition_a = not val_a
    condition_b = not val_b
    result = condition_a and condition_b
    return result

if __name__ == '__main__':
    flag_one = False
    flag_two = False
    output = are_both_variables_false(flag_one, flag_two)
    print(output)