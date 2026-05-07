def check_both_conditions(a: bool, b: bool) -> bool:
    return a and b
if __name__ == '__main__':
    print(check_both_conditions(True, True))
    print(check_both_conditions(True, False))
    print(check_both_conditions(False, True))
    print(check_both_conditions(False, False))