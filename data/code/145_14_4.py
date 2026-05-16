def check_complex_conditions(vars_list, nested_conditions):
    all_true = True
    for condition_group in nested_conditions:
        group_is_true = True
        for var_index, required_value in condition_group:
            if not vars_list[var_index] == required_value:
                group_is_true = False
                break
        if not group_is_true:
            all_true = False
            break
    return all_true
if __name__ == '__main__':
    variables = [True, False, True, True]
    nested_conditions = [
        [(0, True), (2, True)],
        [(1, False), (3, True)]
    ]
    result = check_complex_conditions(variables, nested_conditions)
    print(result)