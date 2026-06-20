def validate_input(boolean_list):
    if not isinstance(boolean_list, list) or len(boolean_list) != 1:
        raise ValueError("Input must be a list containing exactly one boolean value")

def negate_boolean(boolean_list):
    validate_input(boolean_list)
    return not boolean_list[0]

if __name__ == '__main__':
    sample_value = [True]
    negated_value = negate_boolean(sample_value)
    print(f"Negation of {sample_value[0]}: {negated_value}")