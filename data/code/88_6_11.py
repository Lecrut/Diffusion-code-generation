def is_flag_set(flag):
    return flag & 1 == 1

def are_both_flags_true(flag1, flag2):
    return is_flag_set(flag1) and is_flag_set(flag2)

if __name__ == '__main__':
    print(are_both_flags_true(3, 5))
    print(are_both_flags_true(4, 6))