def check_conditions_met(a: bool, b: bool) -> bool:
    return a and b
if __name__ == '__main__':
    print(check_conditions_met(True, True))
    print(check_conditions_met(False, True))
    print(check_conditions_met(True, False))
    print(check_conditions_met(False, False))