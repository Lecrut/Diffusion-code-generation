def test_boolean_conditions(a, b, c):
    if a and b:
        return "Both a and b are True"
    elif not c:
        return "c is False"
    else:
        return "None of the above conditions met"

if __name__ == '__main__':
    print(test_boolean_conditions(True, True, False))
    print(test_boolean_conditions(False, True, True))
    print(test_boolean_conditions(True, False, True))
    print(test_boolean_conditions(False, False, True))