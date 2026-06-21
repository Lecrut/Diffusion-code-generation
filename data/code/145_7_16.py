def evaluate_nested_if_else(conditions):
    result = True
    for condition in conditions:
        if isinstance(condition, tuple) and len(condition) == 3:
            flag, true_branch, false_branch = condition
            if flag:
                result = evaluate_nested_if_else(true_branch)
            else:
                result = evaluate_nested_if_else(false_branch)
        elif isinstance(condition, bool):
            result = condition
    return result

if __name__ == '__main__':
    sample_conditions = [
        (True, [False], []),
        (False, [], [True]),
        (True, [(False, [True], [])], [])
    ]
    print(evaluate_nested_if_else(sample_conditions))