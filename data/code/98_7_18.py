def evaluate_system_state(flag_a, flag_b, flag_c, flag_d):
    MASK_ACTIVE = 1
    MASK_SECURE = 2
    MASK_VALID = 4
    MASK_READY = 8
    
    is_active = bool(flag_a & MASK_ACTIVE)
    is_secure = bool(flag_b & MASK_SECURE)
    is_valid = bool(flag_c & MASK_VALID)
    is_ready = bool(flag_d & MASK_READY)
    
    if is_active and is_secure:
        if is_valid or is_ready:
            return "OPERATIONAL"
        return "SECURE_IDLE"
    
    if is_active or is_secure:
        if is_valid and is_ready:
            return "PARTIAL_ACTIVE"
        return "PARTIAL_SECURE"
    
    if is_valid or is_ready:
        return "STANDBY"
    
    return "OFFLINE"

if __name__ == '__main__':
    status = evaluate_system_state(1, 2, 4, 8)
    print(status)