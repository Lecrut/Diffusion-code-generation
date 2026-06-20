def validate_booleans(a: bool, b: bool) -> None:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values.")

def compare_booleans(flag1: bool, flag2: bool) -> bool:
    validate_booleans(flag1, flag2)
    return flag1 == flag2

if __name__ == '__main__':
    print(compare_booleans(True, True))
    print(compare_booleans(False, False))
    print(compare_booleans(True, False))
    print(compare_booleans(False, True))