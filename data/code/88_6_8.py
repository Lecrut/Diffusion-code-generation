def are_both_true(flag1: int, flag2: int) -> bool:
    return flag1 & 1 == 1 and flag2 & 1 == 1
if __name__ == '__main__':
    print(are_both_true(1, 1))
    print(are_both_true(0, 1))
    print(are_both_true(1, 0))
    print(are_both_true(0, 0))