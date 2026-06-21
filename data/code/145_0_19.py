def check_nested_conditions(a, b, c):
    intermediate = a and b or c
    return intermediate
if __name__ == '__main__':
    print(check_nested_conditions(True, True, False))
    print(check_nested_conditions(False, False, True))
    print(check_nested_conditions(True, False, True))
    print(check_nested_conditions(False, True, False))