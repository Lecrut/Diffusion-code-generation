def toggle_truth_values(input_stream):
    negation_map = {True: False, False: True}
    for current_value in input_stream:
        if current_value in negation_map:
            yield negation_map[current_value]
        else:
            raise ValueError(f"Expected boolean, got {type(current_value)}")

if __name__ == '__main__':
    test_values = [False, True, False, True, False, True]
    toggled_result = list(toggle_truth_values(test_values))
    print(toggled_result)