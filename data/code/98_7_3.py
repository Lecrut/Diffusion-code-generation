def evaluate_system_state(flag_a, flag_b, flag_c, flag_d):
    is_active = (flag_a & 1) == 1
    is_secure = (flag_b & 2) == 2
    is_valid = (flag_c & 4) == 4
    is_ready = (flag_d & 8) == 8

    if is_active and is_secure:
        if is_valid or is_ready:
            return "SYSTEM_OPERATIONAL"
        else:
            return "SYSTEM_SECURE_IDLE"
    elif is_active or is_secure:
        if is_valid and is_ready:
            return "SYSTEM_PARTIAL_ACTIVE"
        else:
            return "SYSTEM_PARTIAL_SECURE"
    else:
        if is_valid or is_ready:
            return "SYSTEM_STANDBY"
        else:
            return "SYSTEM_OFFLINE"

if __name__ == '__main__':
    result = evaluate_system_state(1, 2, 4, 8)
    print(result)