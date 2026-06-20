def evaluate_conditions(conditions):
    result = True
    for condition in conditions:
        if isinstance(condition, tuple) and len(condition) == 2:
            sub_result = evaluate_conditions(condition)
            if not sub_result:
                return False
        elif isinstance(condition, bool):
            result &= condition
        else:
            raise ValueError("Invalid condition type")
    return result

if __name__ == '__main__':
    sample_conditions = (
        (True, False),
        ((True, True), False),
        (True, True)
    )
    print(evaluate_conditions(sample_conditions))