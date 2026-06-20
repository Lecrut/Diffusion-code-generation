TRUE_FLAG = 1

def are_flags_true(flag1: int, flag2: int) -> bool:
    return (flag1 & TRUE_FLAG) == TRUE_FLAG and (flag2 & TRUE_FLAG) == TRUE_FLAG

if __name__ == '__main__':
    print(are_flags_true(3, 5))
    print(are_flags_true(4, 6))