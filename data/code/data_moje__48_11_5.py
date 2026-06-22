def find_max_sensor_reading(sensor_readings):
    if not sensor_readings:
        return None, None
    max_key = None
    max_value = None
    for key, value in sensor_readings.items():
        if max_value is None or value > max_value:
            max_key = key
            max_value = value
    return max_key, max_value

if __name__ == '__main__':
    sensor_readings = {
        'temperature': 23.5,
        'humidity': 45.2,
        'pressure': 1013.25,
        'wind_speed': 12.8,
        'light_intensity': 850.0
    }
    result_key, result_value = find_max_sensor_reading(sensor_readings)
    print(result_key, result_value)