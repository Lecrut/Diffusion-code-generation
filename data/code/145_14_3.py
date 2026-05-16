def check_complex_conditions(vars_list, nested_conditions):
    all_true = True
    for condition_set in nested_conditions:
        all_true = all_true and all(condition_set)
    return all_true
if __name__ == '__main__':
    variables = {
        "A": True,
        "B": False,
        "C": True,
        "D": True
    }
    conditions = [
        (variables["A"], variables["C"]),
        (variables["B"], variables["D"])
    ]
    result = check_complex_conditions(
        [variables["A"], variables["B"], variables["C"], variables["D"]],
        conditions
    )
    print(result)