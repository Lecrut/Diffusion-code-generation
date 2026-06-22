UNIVERSAL_TRUE = True
UNIVERSAL_FALSE = False

def evaluate_boolean_consistency(values):
    if not values:
        return UNIVERSAL_TRUE
    truth_count = 0
    for current_value in values:
        if current_value:
            truth_count += 1
    if truth_count == 0:
        return UNIVERSAL_FALSE
    if truth_count == len(values):
        return UNIVERSAL_TRUE
    return None

if __name__ == '__main__':
    mixed_data = [True, True, False]
    true_data = [True, True, True]
    false_data = [False, False, False]
    empty_data = []

    mixed_result = evaluate_boolean_consistency(mixed_data)
    true_result = evaluate_boolean_consistency(true_data)
    false_result = evaluate_boolean_consistency(false_data)
    empty_result = evaluate_boolean_consistency(empty_data)

    print(mixed_result)
    print(true_result)
    print(false_result)
    print(empty_result)