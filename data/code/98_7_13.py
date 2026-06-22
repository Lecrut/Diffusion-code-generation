def evaluate_system_state(power_on: int, mode_flag: int, safety_override: int, error_code: int) -> str:
    is_powered = bool(power_on & 0x01)
    is_high_mode = bool(mode_flag & 0x02)
    safety_active = bool(safety_override & 0x04)
    has_critical_error = bool(error_code & 0x08)

    if not is_powered:
        return "OFF"

    if has_critical_error and not safety_active:
        return "FAULT"

    if is_high_mode and safety_active:
        return "HIGH_SAFE"

    if is_high_mode:
        return "HIGH_UNSAFE"

    if safety_active:
        return "NORMAL_SAFE"

    return "NORMAL"

if __name__ == '__main__':
    result = evaluate_system_state(1, 2, 4, 0)
    print(result)