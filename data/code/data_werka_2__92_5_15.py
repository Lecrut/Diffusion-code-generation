def toggle_boolean_flags(data_stream):
    negation_map = {True: False, False: True}
    for current_value in data_stream:
        if current_value in negation_map:
            yield negation_map[current_value]
        else:
            raise ValueError("Input must contain boolean values")

if __name__ == '__main__':
    input_flags = [True, True, False, True, False, False, True]
    inverted_flags = list(toggle_boolean_flags(input_flags))
    print(inverted_flags)