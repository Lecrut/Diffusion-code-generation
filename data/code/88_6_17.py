def is_flag_true(flag):
    return flag & 1 == 1

def are_both_flags_true(flag1, flag2):
    if not (is_flag_true(flag1) and is_flag_true(flag2)):
        raise ValueError("Both flags must be integers representing boolean states.")
    return flag1 & 1 == 1 and flag2 & 1 == 1

if __name__ == '__main__':
    print(are_both_flags_true(3, 5))
    print(are_both_flags_true(4, 6))