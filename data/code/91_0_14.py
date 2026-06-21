def negate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    truth_table = {True: False, False: True}
    return truth_table[value]

if __name__ == '__main__':
    sample_input_1 = True
    sample_input_2 = False
    output_1 = negate_boolean(sample_input_1)
    output_2 = negate_boolean(sample_input_2)
    print(output_1)
    print(output_2)