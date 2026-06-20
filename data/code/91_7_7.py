def validate_input(input_list):
    if not isinstance(input_list, list) or len(input_list) != 1:
        raise ValueError("Input must be a list containing exactly one element.")
    if not isinstance(input_list[0], bool):
        raise TypeError("The single element in the list must be a boolean value.")

def negate_boolean(boolean_list):
    validate_input(boolean_list)
    return not boolean_list[0]

if __name__ == '__main__':
    sample_value = [True]
    negated_value = negate_boolean(sample_value)
    print(f"Negation of {sample_value[0]}: {negated_value}")