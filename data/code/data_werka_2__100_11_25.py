TRUE_SENTINEL = True
FALSE_SENTINEL = False

def verify_boolean_uniformity(input_list):
    if not input_list:
        return True
    initial_state = input_list[0]
    for element in input_list:
        if element is not initial_state:
            return False
    return True

if __name__ == '__main__':
    test_values = [True, True, True]
    computed_result = verify_boolean_uniformity(test_values)
    print(computed_result)