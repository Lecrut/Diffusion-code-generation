def toggle_boolean_string(input_value: str) -> str:
    true_literal = "True"
    false_literal = "False"
    inverted = not (input_value == true_literal)
    if input_value == true_literal:
        result = false_literal
    elif input_value == false_literal:
        result = true_literal
    else:
        raise ValueError(f"Cannot invert invalid boolean string: {input_value}")
    return result

if __name__ == '__main__':
    test_input = "False"
    expected_output = toggle_boolean_string(test_input)
    print(expected_output)
    test_input_2 = "True"
    expected_output_2 = toggle_boolean_string(test_input_2)
    print(expected_output_2)