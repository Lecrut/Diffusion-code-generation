def check_conditions(conditions):
    if not conditions:
        return True
    result = True
    for condition in conditions:
        result = result and condition
    return result
if __name__ == '__main__':
    test_conditions_1 = [True, True, False]
    result_1 = check_conditions(test_conditions_1)
    print(f"Test 1: {test_conditions_1}, Result: {result_1}")
    test_conditions_2 = [True, True, True]
    result_2 = check_conditions(test_conditions_2)
    print(f"Test 2: {test_conditions_2}, Result: {result_2}")
    test_conditions_3 = [False, True, False]
    result_3 = check_conditions(test_conditions_3)
    print(f"Test 3: {test_conditions_3}, Result: {result_3}")
    test_conditions_4 = []
    result_4 = check_conditions(test_conditions_4)
    print(f"Test 4: {test_conditions_4}, Result: {result_4}")
    test_conditions_5 = [True]
    result_5 = check_conditions(test_conditions_5)
    print(f"Test 5: {test_conditions_5}, Result: {result_5}")