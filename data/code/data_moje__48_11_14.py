def find_max_sensor_reading(sensor_readings):
    if not sensor_readings:
        raise ValueError("Sensor readings dictionary cannot be empty")
    max_key = None
    max_value = None
    for key, value in sensor_readings.items():
        if max_value is None or value > max_value:
            max_key = key
            max_value = value
    return max_key, max_value

if __name__ == '__main__':
    hard_coded_readings = {
        "sensor_01": 23.5,
        "sensor_02": 45.2,
        "sensor_03": 12.8,
        "sensor_04": 67.9,
        "sensor_05": 34.1
    }
    result_key, result_value = find_max_sensor_reading(hard_coded_readings)
    print(result_key, result_value)