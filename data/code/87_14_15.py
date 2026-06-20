def validate_inputs(flag1: bool, flag2: bool) -> None:
    if not isinstance(flag1, bool) or not isinstance(flag2, bool):
        raise ValueError("Both inputs must be boolean values.")

def exclusive_truthiness(flag1: bool, flag2: bool) -> bool:
    validate_inputs(flag1, flag2)
    return flag1 ^ flag2

if __name__ == '__main__':
    print(exclusive_truthiness(True, False))
    print(exclusive_truthiness(False, True))
    print(exclusive_truthiness(True, True))
    print(exclusive_truthiness(False, False))