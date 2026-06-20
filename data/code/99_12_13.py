def nested_boolean_conditions(a, b, c):
    return a or (b and (not c))
if __name__ == '__main__':
    print(nested_boolean_conditions(True, False, True))
    print(nested_boolean_conditions(False, True, False))
    print(nested_boolean_conditions(False, False, True))