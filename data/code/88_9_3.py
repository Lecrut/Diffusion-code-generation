def check_both_true(flag1, flag2):
    return (flag1 & flag2) == flag1
if __name__ == '__main__':
    flag_a = 3
    flag_b = 3
    result_ab = check_both_true(flag_a, flag_b)
    print(result_ab)
    flag_c = 1
    flag_d = 2
    result_cd = check_both_true(flag_c, flag_d)
    print(result_cd)
    flag_e = 0
    flag_f = 1
    result_ef = check_both_true(flag_e, flag_f)
    print(result_ef)