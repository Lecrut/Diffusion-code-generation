def are_both_flags_true(flag1, flag2):
    return flag1 & 1 == 1 and flag2 & 1 == 1
if __name__ == '__main__':
    print(are_both_flags_true(3, 5))
    print(are_both_flags_true(2, 4))