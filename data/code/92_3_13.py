def invert_boolean_sequence(input_sequence):
    inverted_values = []
    for current_value in input_sequence:
        if current_value:
            inverted_values.append(False)
        else:
            inverted_values.append(True)
    return inverted_values

if __name__ == '__main__':
    test_data = [True, True, False, True, False, False]
    computed_result = invert_boolean_sequence(test_data)
    print(computed_result)