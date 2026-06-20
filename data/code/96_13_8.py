def evaluate_conditions(conditions):
    result = False
    for condition in conditions:
        if isinstance(condition, tuple):
            sub_result = evaluate_conditions(condition)
        else:
            sub_result = condition
        result |= sub_result
    return result

if __name__ == '__main__':
    sample_conditions = (
        True,
        (False, True),
        ((True, False), False)
    )
    print(evaluate_conditions(sample_conditions))