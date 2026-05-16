def system_state_checker(flag_a, flag_b, flag_c, flag_d):
    state = 0
    if flag_a:
        state |= 1
    if flag_b:
        state |= 2
    if flag_c:
        state |= 4
    if flag_d:
        state |= 8
    return state
if __name__ == '__main__':
    flag_a_val = 1
    flag_b_val = 0
    flag_c_val = 1
    flag_d_val = 1
    result = system_state_checker(flag_a_val, flag_b_val, flag_c_val, flag_d_val)
    print(result)