def invert_boolean_sequence(input_sequence):
    inverted = []
    for element in input_sequence:
        if element:
            inverted.append(False)
        else:
            inverted.append(True)
    return inverted

if __name__ == '__main__':
    source_data = [True, True, False, False, True]
    transformed_data = invert_boolean_sequence(source_data)
    print(transformed_data)