def system_status_checker(power_on, sensor_ok, alarm_active, battery_low):
    if power_on and sensor_ok and not alarm_active and not battery_low:
        return "System Nominal"
    elif power_on and sensor_ok and alarm_active:
        return "Warning: Alarm Active"
    elif power_on and not sensor_ok:
        return "Error: Sensor Failure"
    elif power_on and not alarm_active and battery_low:
        return "Warning: Low Battery"
    elif not power_on:
        return "System Off"
    else:
        return "Unknown State"
if __name__ == '__main__':
    print(system_status_checker(True, True, False, False))
    print(system_status_checker(True, True, True, False))
    print(system_status_checker(True, False, False, False))
    print(system_status_checker(True, True, False, True))
    print(system_status_checker(False, True, False, False))
    print(system_status_checker(False, False, True, True))