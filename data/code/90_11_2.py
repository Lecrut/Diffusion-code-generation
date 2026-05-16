def check_condition(*conditions):
    return any(conditions)
if __name__ == '__main__':
    print(check_condition(False, False, True))
    print(check_condition(False, False, False))
    print(check_condition(True, False, False))
    print(check_condition(True, True, False))
    print(check_condition(False))
    print(check_condition(True, True, True, False))