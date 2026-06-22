def negate_boolean_sequence(values):
    negation_map = {True: False, False: True}
    for current_value in values:
        if current_value in negation_map:
            yield negation_map[current_value]
        else:
            raise ValueError("Sequence must contain only boolean values")

if __name__ == '__main__':
    input_sequence = [False, True, False, True, False]
    inverted_sequence = list(negate_boolean_sequence(input_sequence))
    print(inverted_sequence)