def check_boolean_array(boolean_array):
    lookup_table = {True: 'exists', False: 'absent'}
    if not boolean_array:
        return lookup_table[False]
    for element in boolean_array:
        if element is True:
            return lookup_table[True]
    return lookup_table[False]

if __name__ == '__main__':
    test_data = [False, False, False, True, False]
    output = check_boolean_array(test_data)
    print(output)