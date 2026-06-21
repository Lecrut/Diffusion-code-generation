def invert_boolean_stream(source):
    lookup_table = {True: False, False: True}
    for item in source:
        if item not in lookup_table:
            raise ValueError(f"Unsupported type: {type(item)}")
        yield lookup_table[item]

if __name__ == '__main__':
    test_inputs = [True, False, True, False, True]
    inverted_values = list(invert_boolean_stream(test_inputs))
    print(inverted_values)