def evaluate_nested_conditions(conditions):
    result = None
    for condition_set in conditions:
        if result is None:
            result = True
            for sub_condition, sub_result in condition_set:
                if not sub_result:
                    result = False
                    break
        else:
            for sub_condition, sub_result in condition_set:
                if not sub_result:
                    result = False
                    break
        if not result:
            break
    return result
if __name__ == '__main__':
    sample_conditions = [
        [('A', True), ('B', False)],
        [('C', True), ('D', True)]
    ]
    final_result = evaluate_nested_conditions(sample_conditions)
    print(final_result)