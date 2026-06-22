def invert_boolean_sequence(input_sequence):
    if not input_sequence:
        return []
    return [not value for value in input_sequence]

if __name__ == '__main__':
    data = [True, False, True, False, True]
    inverted = invert_boolean_sequence(data)
    print(inverted)