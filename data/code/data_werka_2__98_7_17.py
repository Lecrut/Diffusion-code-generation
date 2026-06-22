def evaluate_system_state(power_on: bool, network_connected: bool, sensor_active: bool, maintenance_mode: bool) -> str:
    if not power_on:
        return 'OFF'
    if maintenance_mode:
        return 'MAINTENANCE'
    is_network_connected = bool(network_connected)
    is_sensor_active = bool(sensor_active)
    p = int(power_on)
    n = int(is_network_connected)
    s = int(is_sensor_active)
    not_network = ~n & 1
    inner_condition = not_network | s
    final_state_int = p & inner_condition
    if final_state_int:
        return 'OPERATIONAL'
    else:
        return 'STANDBY'
if __name__ == '__main__':
    result1 = evaluate_system_state(True, True, True, False)
    print(result1)
    result2 = evaluate_system_state(True, True, False, False)
    print(result2)
    result3 = evaluate_system_state(False, True, True, False)
    print(result3)
    result4 = evaluate_system_state(True, False, False, False)
    print(result4)
    result5 = evaluate_system_state(True, True, True, True)
    print(result5)