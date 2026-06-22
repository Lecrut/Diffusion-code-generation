def evaluate_system_state(flag_a: bool, flag_b: bool, flag_c: bool, flag_d: bool) -> str:
    val_a = int(flag_a)
    val_b = int(flag_b)
    val_c = int(flag_c)
    val_d = int(flag_d)
    high_priority = val_a and (val_b or val_c)
    medium_priority = val_d and (not val_a)
    low_priority = (val_b and val_c) and (not high_priority) and (not medium_priority)
    if high_priority:
        return 'CRITICAL'
    elif medium_priority:
        return 'WARNING'
    elif low_priority:
        return 'NORMAL'
    else:
        return 'IDLE'
if __name__ == '__main__':
    result1 = evaluate_system_state(True, True, False, False)
    print(result1)
    result2 = evaluate_system_state(False, False, False, True)
    print(result2)
    result3 = evaluate_system_state(False, True, True, False)
    print(result3)
    result4 = evaluate_system_state(False, False, False, False)
    print(result4)