def find_max_sensor_reading(readings):
    if not readings:
        return None, None
    max_key = None
    max_value = -float('inf')
    for key, value in readings.items():
        if value > max_value:
            max_key = key
            max_value = value
    return max_key, max_value

if __name__ == '__main__':
    sensor_data = {
        "temp_1": 23.5,
        "temp_2": 24.8,
        "temp_3": 19.2,
        "pressure_1": 1013.25,
        "humidity_1": 45.6,
        "humidity_2": 67.3
    }
    result_key, result_value = find_max_sensor_reading(sensor_data)
    print(result_key, result_value)