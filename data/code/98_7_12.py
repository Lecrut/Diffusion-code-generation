def validate_flags(flag_a, flag_b, flag_c, flag_d):
    if not isinstance(flag_a, bool) or not isinstance(flag_b, bool) or not isinstance(flag_c, bool) or not isinstance(flag_d, bool):
        raise ValueError("All flags must be boolean values.")

def calculate_state(flag_a, flag_b, flag_c, flag_d):
    state = 0
    if flag_a:
        state |= 1 << 0
    if flag_b:
        state |= 1 << 1
    if flag_c:
        state |= 1 << 2
    if flag_d:
        state |= 1 << 3
    return state

def system_state_checker(flag_a, flag_b, flag_c, flag_d):
    validate_flags(flag_a, flag_b, flag_c, flag_d)
    return calculate_state(flag_a, flag_b, flag_c, flag_d)

if __name__ == '__main__':
    flag_a_val = True
    flag_b_val = False
    flag_c_val = True
    flag_d_val = True
    result = system_state_checker(flag_a_val, flag_b_val, flag_c_val, flag_d_val)
    print(result)