def determine_system_state(flag_a, flag_b, flag_c):
    state = 0
    if flag_a:
        state |= 0b0001
    if flag_b:
        state |= 0b0010
    if flag_c:
        state |= 0b0100
    return state

if __name__ == '__main__':
    print(determine_system_state(True, False, True))