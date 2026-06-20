def check_complex_condition(a, b, c, d):
    if not all((isinstance(x, bool) for x in [a, b, c, d])):
        return False
    if a and b:
        if c or d:
            return True
    elif not a and (not b):
        if not c and (not d):
            return True
    return False
if __name__ == '__main__':
    print(check_complex_condition(True, True, False, False))
    print(check_complex_condition(False, False, True, True))
    print(check_complex_condition(True, False, True, False))
    print(check_complex_condition(False, True, False, True))