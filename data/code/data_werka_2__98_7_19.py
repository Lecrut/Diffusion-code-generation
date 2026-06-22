def evaluate_system_state(flag_a: bool, flag_b: bool, flag_c: bool, flag_d: bool) -> str:
    mask_1 = flag_a << 3 | flag_b << 2 | flag_c << 1 | flag_d << 0
    critical_active = flag_a or flag_b
    monitoring_active = flag_c or flag_d
    pattern_1 = mask_1 & 5 == 5
    pattern_2 = mask_1 & 6 == 6
    if critical_active and monitoring_active:
        if pattern_1 or pattern_2:
            return 'CRITICAL_MONITORING_PATTERN'
        else:
            return 'FULLY_ACTIVE'
    elif critical_active:
        return 'CRITICAL_ONLY'
    elif monitoring_active:
        return 'MONITORING_ONLY'
    else:
        return 'INACTIVE'
if __name__ == '__main__':
    result = evaluate_system_state(True, False, True, True)
    print(result)
    result2 = evaluate_system_state(False, True, False, False)
    print(result2)
    result3 = evaluate_system_state(False, False, False, False)
    print(result3)
    result4 = evaluate_system_state(True, True, False, False)
    print(result4)