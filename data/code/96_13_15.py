def evaluate_conditions(conditions):
    result = True
    for condition in conditions:
        if isinstance(condition, tuple) and len(condition) == 2:
            sub_result = evaluate_conditions(condition)
            result &= sub_result
        else:
            result &= bool(condition)
    return result

if __name__ == '__main__':
    sample_conditions = (
        (True, False),
        ((True, True), False),
        (True, (False, True)),
        (((True, False), True), False)
    )
    print(evaluate_conditions(sample_conditions))