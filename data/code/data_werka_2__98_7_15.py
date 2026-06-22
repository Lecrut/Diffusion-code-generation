def determine_system_state(power_on: bool, network_connected: bool, maintenance_mode: bool, critical_error: bool) -> str:
    power_flag = 1 if power_on else 0
    network_flag = 2 if network_connected else 0
    maintenance_flag = 4 if maintenance_mode else 0
    error_flag = 8 if critical_error else 0
    combined_state = power_flag | network_flag | maintenance_flag | error_flag
    if critical_error:
        return 'CRITICAL_FAILURE'
    if maintenance_mode:
        if power_on and network_connected:
            return 'MAINTENANCE_ACTIVE'
        elif power_on:
            return 'MAINTENANCE_POWER_ONLY'
        else:
            return 'MAINTENANCE_OFFLINE'
    if power_on:
        if network_connected:
            return 'NORMAL_OPERATION'
        else:
            return 'LOCAL_MODE'
    if network_connected:
        return 'STANDBY_NETWORK'
    return 'OFFLINE'
if __name__ == '__main__':
    result = determine_system_state(True, True, False, False)
    print(result)