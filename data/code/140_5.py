def evaluate_nested_conditions(conditions):
    result = 0
    for condition_set in conditions:
        if not condition_set:
            continue
        current_value = True
        for sub_condition in condition_set:
            if not sub_condition:
                current_value = False
                break
        if current_value:
            result += 1
    return result
if __name__ == '__main__':
    sample_conditions = [
        (True, False),
        (True, True),
        (False, False, True),
        (True, True, False),
        (),
        (True, True, True)
    ]
    final_result = evaluate_nested_conditions(sample_conditions)
    print(final_result)