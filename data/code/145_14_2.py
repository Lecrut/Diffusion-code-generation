def check_complex_conditions(vars_list, nested_conditions):
    all_true = True
    for condition_set in nested_conditions:
        all_true = all_true and all(vars_list[i] == condition_set[0] for i in range(len(condition_set)))
    return all_true
if __name__ == '__main__':
    variables = [True, False, True]
    conditions = [
        (True, True),
        (False, True),
        (True, False)
    ]
    result = check_complex_conditions(variables, conditions)
    print(result)