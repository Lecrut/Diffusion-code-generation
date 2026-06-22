def find_max_sensor_reading(readings):
    if not readings:
        return None
    max_key = None
    max_value = None
    for key, value in readings.items():
        if max_value is None or value > max_value:
            max_value = value
            max_key = key
    return (max_key, max_value)

if __name__ == '__main__':
    sensor_data = {
        "temp_01": 23.5,
        "temp_02": 24.1,
        "humidity_01": 45.0,
        "pressure_01": 1013.25,
        "temp_03": 22.8,
        "vibration_01": 0.05
    }
    result = find_max_sensor_reading(sensor_data)
    print(result)