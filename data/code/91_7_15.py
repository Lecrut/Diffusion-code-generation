def validate_input(boolean_list):
    if not isinstance(boolean_list, list) or len(boolean_list) != 1:
        raise ValueError("Input must be a list containing exactly one element.")
    if not isinstance(boolean_list[0], bool):
        raise ValueError("The single element in the list must be a boolean.")

def negate_boolean_value(value: bool) -> bool:
    return not value

if __name__ == '__main__':
    sample_value = [True]
    validate_input(sample_value)
    negated_value = negate_boolean_value(sample_value[0])
    print(f"Negation of {sample_value[0]}: {negated_value}")