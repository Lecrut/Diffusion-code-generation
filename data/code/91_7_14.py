def invert_boolean_element(input_list):
    NEGATION_MAP = {True: False, False: True}
    if len(input_list) != 1:
        raise ValueError("List must contain exactly one element")
    element = input_list[0]
    if element not in NEGATION_MAP:
        raise ValueError("Element must be a boolean")
    return NEGATION_MAP[element]

if __name__ == '__main__':
    test_data = [True]
    output = invert_boolean_element(test_data)
    print(output)