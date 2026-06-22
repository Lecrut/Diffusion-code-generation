def find_max_sensor_reading(sensor_readings):
    max_key = None
    max_value = float('-inf')
    for key, value in sensor_readings.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key, max_value

if __name__ == '__main__':
    sensor_data = {
        'temperature': 22.5,
        'humidity': 45.0,
        'pressure': 1013.25,
        'light': 850.7,
        'wind_speed': 12.3,
        'uv_index': 6.8
    }
    result_key, result_value = find_max_sensor_reading(sensor_data)
    print(result_key)
    print(result_value)