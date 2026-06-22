def toggle_boolean_string(input_str: str) -> str:
    true_literal = 'True'
    false_literal = 'False'
    if input_str == true_literal:
        return false_literal
    if input_str == false_literal:
        return true_literal
    raise ValueError(f"Cannot toggle invalid boolean string: {input_str}")

if __name__ == '__main__':
    sample_input = 'False'
    result = toggle_boolean_string(sample_input)
    print(result)
    sample_input_2 = 'True'
    result_2 = toggle_boolean_string(sample_input_2)
    print(result_2)