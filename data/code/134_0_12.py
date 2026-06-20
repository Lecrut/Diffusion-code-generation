def are_conditions_mutually_exclusive(a, b, c):
    return a + b + c == 1
if __name__ == '__main__':
    result_1 = are_conditions_mutually_exclusive(True, False, True)
    print(result_1)
    result_2 = are_conditions_mutually_exclusive(False, True, False)
    print(result_2)
    result_3 = are_conditions_mutually_exclusive(True, True, False)
    print(result_3)
    result_4 = are_conditions_mutually_exclusive(True, True, True)
    print(result_4)