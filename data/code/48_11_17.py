def find_max_sensor_reading(sensor_readings):
    if not sensor_readings:
        return None, None
    max_key = None
    max_value = float('-inf')
    for key, value in sensor_readings.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key, max_value

if __name__ == '__main__':
    sensor_data = {
        'temp_sensor_1': 23.5,
        'pressure_sensor_A': 101.3,
        'temp_sensor_2': 28.9,
        'humidity_sensor_X': 45.0,
        'pressure_sensor_B': 98.7,
        'temp_sensor_3': 31.2
    }
    result_key, result_value = find_max_sensor_reading(sensor_data)
    print(result_key, result_value)