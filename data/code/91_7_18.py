def validate_input(value_list):
    if len(value_list) != 1:
        raise ValueError("Input list must contain exactly one element")
    if not isinstance(value_list[0], bool):
        raise ValueError("The single element in the list must be a boolean value")

def negate_boolean(boolean_list):
    validate_input(boolean_list)
    return not boolean_list[0]

if __name__ == '__main__':
    sample_value = [True]
    negated_value = negate_boolean(sample_value)
    print(f"Negation of {sample_value[0]}: {negated_value}")