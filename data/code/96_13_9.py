def evaluate_conditions(conditions):
    result = True
    for condition in conditions:
        if isinstance(condition, tuple) and len(condition) == 2:
            sub_result = evaluate_conditions(condition)
        else:
            sub_result = condition
        result = result and sub_result
    return result

if __name__ == '__main__':
    sample_conditions = ((True, False), (False, True), (True, True))
    print(evaluate_conditions(sample_conditions))