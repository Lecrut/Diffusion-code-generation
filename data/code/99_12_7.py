def nested_boolean_conditions(a, b, c):
    return a and (b or not c)
if __name__ == '__main__':
    print(nested_boolean_conditions(True, False, True))
    print(nested_boolean_conditions(True, True, False))