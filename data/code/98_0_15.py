def test_boolean_conditions(a, b, c):
    if a and b:
        return "Both a and b are True"
    elif a or c:
        return "Either a or c is True"
    else:
        return "None of the conditions are met"

if __name__ == '__main__':
    print(test_boolean_conditions(True, False, True))
    print(test_boolean_conditions(False, True, False))
    print(test_boolean_conditions(False, False, False))