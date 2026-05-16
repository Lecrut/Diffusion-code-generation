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
    flag_a = True
    flag_b = False
    flag_c = True
    flag_d = True
    result = system_state_checker(flag_a, flag_b, flag_c, flag_d)
    print(result)