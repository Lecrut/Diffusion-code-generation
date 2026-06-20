def validate_flags(flag1, flag2):
    if not (isinstance(flag1, int) and isinstance(flag2, int)):
        raise ValueError("Both flags must be integers")
    return True

def combine_flags(flag1, flag2):
    validate_flags(flag1, flag2)
    return flag1 | flag2

if __name__ == '__main__':
    test_flag1 = 5
    test_flag2 = 3
    result = combine_flags(test_flag1, test_flag2)
    print(result)