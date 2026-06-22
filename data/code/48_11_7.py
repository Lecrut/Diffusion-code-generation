def find_max_sensor_reading(sensors):
    max_key = None
    max_value = float('-inf')
    for key, value in sensors.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key, max_value

if __name__ == '__main__':
    sensor_data = {
        'temperature_1': 23.5,
        'humidity_1': 45.2,
        'pressure_1': 1013.25,
        'temperature_2': 25.1,
        'humidity_2': 50.8,
        'pressure_2': 1012.9,
        'wind_speed': 15.3,
        'rainfall': 0.0
    }
    key, value = find_max_sensor_reading(sensor_data)
    print(key, value)