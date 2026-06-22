def validate_boolean_inputs(value_one, value_two):
    if not isinstance(value_one, bool):
        raise ValueError("First input must be a boolean")
    if not isinstance(value_two, bool):
        raise ValueError("Second input must be a boolean")
    return True

def are_both_false(first_input, second_input):
    validate_boolean_inputs(first_input, second_input)
    negated_first = bool(not first_input)
    negated_second = bool(not second_input)
    combined_result = negated_first and negated_second
    return combined_result

if __name__ == '__main__':
    test_val_a = False
    test_val_b = False
    computed_value = are_both_false(test_val_a, test_val_b)
    print(computed_value)