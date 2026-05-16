def check_conditions(conditions):
    if not conditions:
        return True
    result = True
    for condition in conditions:
        result = result and condition
    return result
if __name__ == '__main__':
    test_conditions_1 = [True, True, False]
    print(f"Test 1: {check_conditions(test_conditions_1)}")
    test_conditions_2 = [True, True, True]
    print(f"Test 2: {check_conditions(test_conditions_2)}")
    test_conditions_3 = [False, True, False]
    print(f"Test 3: {check_conditions(test_conditions_3)}")
    test_conditions_4 = []
    print(f"Test 4: {check_conditions(test_conditions_4)}")
    test_conditions_5 = [True]
    print(f"Test 5: {check_conditions(test_conditions_5)}")