def evaluate_system_state(power_on: int, mode: int, sensor_active: int, safety_override: int) -> str:
    is_powered = power_on & 1
    is_mode_active = mode >> 1 & 1
    is_sensor_active = sensor_active >> 2 & 1
    is_override_active = safety_override >> 3 & 1
    if not is_powered:
        return 'OFF'
    if is_override_active:
        return 'OVERRIDE'
    if is_mode_active and is_sensor_active:
        return 'ACTIVE'
    if is_mode_active or is_sensor_active:
        return 'STANDBY'
    return 'IDLE'
if __name__ == '__main__':
    power = 1
    mode = 2
    sensor = 4
    override = 0
    result = evaluate_system_state(power, mode, sensor, override)
    print(result)