def find_max_sensor_reading(sensor_readings: dict) -> tuple:
    max_key = None
    max_value = None
    is_first = True
    for key, value in sensor_readings.items():
        if is_first:
            max_key = key
            max_value = value
            is_first = False
        elif value > max_value:
            max_key = key
            max_value = value
    return max_key, max_value

if __name__ == '__main__':
    sensors = {
        "temp_1": 98.6,
        "temp_2": 102.3,
        "humidity_1": 45.0,
        "pressure_1": 1013.25
    }
    result_key, result_value = find_max_sensor_reading(sensors)
    print(result_key, result_value)