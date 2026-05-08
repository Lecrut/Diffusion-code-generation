def determine_system_state(flag_a, flag_b, flag_c):
    if flag_a and flag_b and not flag_c:
        return "State_A_B_Only"
    elif flag_a and flag_b and flag_c:
        return "State_A_B_C_Full"
    elif flag_a and not flag_b and flag_c:
        return "State_A_C_Only"
    elif not flag_a and flag_b and flag_c:
        return "State_B_C_Only"
    elif flag_a and not flag_b and not flag_c:
        return "State_A_Only"
    elif not flag_a and not flag_b and flag_c:
        return "State_C_Only"
    elif not flag_a and not flag_b and not flag_c:
        return "State_None"
    else:
        return "Error_Unhandled"
if __name__ == '__main__':
    print(determine_system_state(True, True, False))
    print(determine_system_state(True, True, True))
    print(determine_system_state(True, False, True))
    print(determine_system_state(False, True, True))
    print(determine_system_state(True, False, False))
    print(determine_system_state(False, False, True))
    print(determine_system_state(False, False, False))