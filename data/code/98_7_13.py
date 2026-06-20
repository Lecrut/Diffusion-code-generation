def determine_system_state(flag_a, flag_b, flag_c):
    state = 0
    if flag_a:
        state |= 1 << 0
    if flag_b:
        state |= 1 << 1
    if flag_c:
        state |= 1 << 2
    if state & 3 == 3:
        return 'Critical'
    elif state & 1:
        return 'Warning'
    else:
        return 'Normal'
if __name__ == '__main__':
    print(determine_system_state(True, True, False))
    print(determine_system_state(False, True, False))
    print(determine_system_state(False, False, False))