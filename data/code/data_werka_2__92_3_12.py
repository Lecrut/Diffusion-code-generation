TRUE_VAL = True
FALSE_VAL = False

def invert_boolean_list(input_list):
    return [FALSE_VAL if item else TRUE_VAL for item in input_list]

if __name__ == '__main__':
    initial_values = [True, True, False, True, False, False]
    inverted_values = invert_boolean_list(initial_values)
    print(inverted_values)