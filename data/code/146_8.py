def determine_system_state(flag_a, flag_b, flag_c):
    if flag_a and flag_b and not flag_c:
        return "State_A_B_Not_C"
    elif flag_a and flag_c:
        return "State_A_C"
    elif flag_b and flag_c:
        return "State_B_C"
    elif flag_a:
        return "State_A"
    elif flag_b:
        return "State_B"
    elif flag_c:
        return "State_C"
    else:
        return "State_None"
if __name__ == '__main__':
    print(determine_system_state(True, True, False))
    print(determine_system_state(True, False, True))
    print(determine_system_state(False, True, True))
    print(determine_system_state(True, True, True))
    print(determine_system_state(False, False, False))
    print(determine_system_state(True, False, False))
    print(determine_system_state(False, True, False))
    print(determine_system_state(False, False, True))