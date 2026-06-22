def evaluate_system_state(power_on: bool, mode: int, sensor_active: bool, error_code: int) -> str:
    is_ready = power_on and mode & 1 and sensor_active
    has_critical_error = error_code & 32768
    has_warning = error_code & 16384
    if has_critical_error:
        return 'CRITICAL_FAILURE'
    if not power_on:
        return 'OFF'
    if not sensor_active:
        return 'SENSOR_OFF'
    if is_ready:
        if has_warning:
            return 'WARNING_READY'
        return 'READY'
    return 'STANDBY'
if __name__ == '__main__':
    result1 = evaluate_system_state(True, 1, True, 0)
    print(result1)
    result2 = evaluate_system_state(True, 1, True, 32768)
    print(result2)
    result3 = evaluate_system_state(False, 1, True, 0)
    print(result3)
    result4 = evaluate_system_state(True, 0, True, 0)
    print(result4)
    result5 = evaluate_system_state(True, 1, False, 16384)
    print(result5)