def evaluate_system_state(flag_a, flag_b, flag_c, flag_d):
    a_active = flag_a & 1
    b_active = (flag_b & 2) >> 1
    c_active = (flag_c & 4) >> 2
    d_active = (flag_d & 8) >> 3
    if a_active and b_active and c_active and d_active:
        return 'FULLY_OPERATIONAL'
    active_count = a_active + b_active + c_active + d_active
    if active_count >= 2:
        return 'PARTIALLY_OPERATIONAL'
    if a_active and (not b_active) and (not c_active) and (not d_active):
        return 'STANDBY'
    if not a_active and (not b_active) and (not c_active) and d_active:
        return 'EMERGENCY_STOP'
    if active_count == 1:
        return 'MINIMAL_ACTIVITY'
    return 'OFFLINE'
if __name__ == '__main__':
    result1 = evaluate_system_state(1, 2, 4, 8)
    print(result1)
    result2 = evaluate_system_state(1, 0, 0, 0)
    print(result2)
    result3 = evaluate_system_state(0, 0, 0, 0)
    print(result3)
    result4 = evaluate_system_state(1, 2, 0, 0)
    print(result4)
    result5 = evaluate_system_state(0, 0, 0, 8)
    print(result5)