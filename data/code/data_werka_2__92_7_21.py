def invert_boolean(value: bool) -> bool:
    truth_table = {True: False, False: True}
    return truth_table[value]

if __name__ == '__main__':
    input_bool = False
    inverted_result = invert_boolean(input_bool)
    print(inverted_result)