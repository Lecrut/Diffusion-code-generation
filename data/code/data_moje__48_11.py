def find_max_sensor_reading(sensors):
    if not sensors:
        return None, None
    max_key = None
    max_value = None
    for key, value in sensors.items():
        if max_value is None or value > max_value:
            max_value = value
            max_key = key
    return max_key, max_value

if __name__ == '__main__':
    hard_coded_sensors = {
        "temp_01": 23.5,
        "temp_02": 28.9,
        "humidity_01": 45.2,
        "pressure_01": 101.3,
        "temp_03": 31.4,
        "humidity_02": 60.1
    }
    key, value = find_max_sensor_reading(hard_coded_sensors)
    print(key, value)