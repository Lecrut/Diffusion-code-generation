def validate_boolean_inputs(flag1: bool, flag2: bool) -> None:
    if not isinstance(flag1, bool) or not isinstance(flag2, bool):
        raise ValueError("Both inputs must be boolean values.")

def check_boolean_equality(flag1: bool, flag2: bool) -> bool:
    validate_boolean_inputs(flag1, flag2)
    return flag1 == flag2

if __name__ == '__main__':
    print(check_boolean_equality(True, True))
    print(check_boolean_equality(False, False))
    print(check_boolean_equality(True, False))
    print(check_boolean_equality(False, True))