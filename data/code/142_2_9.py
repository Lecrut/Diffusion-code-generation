def validate_booleans(a: bool, b: bool) -> None:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values.")

def check_boolean_equality(flag1: bool, flag2: bool) -> bool:
    validate_booleans(flag1, flag2)
    return flag1 == flag2

if __name__ == '__main__':
    sample1 = True
    sample2 = False
    print(check_boolean_equality(sample1, sample2))
    print(check_boolean_equality(False, False))