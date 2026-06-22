def find_max_sensor_reading(sensor_data):
    if not sensor_data:
        return None
    max_key = None
    max_value = float('-inf')
    for key, value in sensor_data.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key, max_value

if __name__ == '__main__':
    sensor_readings = {
        'temperature_01': 22.5,
        'humidity_02': 45.0,
        'pressure_03': 1013.25,
        'temperature_04': 23.1,
        'humidity_05': 50.5,
        'light_intensity_06': 750,
        'noise_level_07': 60.2
    }
    result = find_max_sensor_reading(sensor_readings)
    print(result)