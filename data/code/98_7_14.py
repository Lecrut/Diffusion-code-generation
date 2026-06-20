def determine_system_state(flag_a: bool, flag_b: bool, flag_c: bool) -> str:
    state = 0
    if flag_a:
        state |= 1 << 0
    if flag_b:
        state |= 1 << 1
    if flag_c:
        state |= 1 << 2

    if (state & (1 << 0)) and not (state & (1 << 1)):
        return "State A active"
    elif (state & (1 << 1)) and not (state & (1 << 2)):
        return "State B active"
    elif (state & (1 << 2)) and not (state & (1 << 0)):
        return "State C active"
    else:
        return "No state active"

if __name__ == '__main__':
    print(determine_system_state(True, False, False))
    print(determine_system_state(False, True, False))
    print(determine_system_state(False, False, True))
    print(determine_system_state(True, True, False))
    print(determine_system_state(False, True, True))
    print(determine_system_state(True, False, True))
    print(determine_system_state(True, True, True))