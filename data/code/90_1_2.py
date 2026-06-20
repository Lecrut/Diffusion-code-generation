def check_or_condition(a, b):
    return a or b

if __name__ == '__main__':
    print(check_or_condition(True, False))
    print(check_or_condition(False, True))
    print(check_or_condition(True, True))
    print(check_or_condition(False, False))