def validate_flags(flag1: bool, flag2: bool) -> bool:
    if not isinstance(flag1, bool) or not isinstance(flag2, bool):
        raise ValueError("Both inputs must be boolean values.")
    return True

def combine_flags(flag1: bool, flag2: bool) -> bool:
    if not validate_flags(flag1, flag2):
        raise ValueError("Invalid input types for flags.")
    return flag1 and flag2

if __name__ == '__main__':
    result = combine_flags(True, False)
    print(result)