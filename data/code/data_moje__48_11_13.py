def find_max_sensor_reading(sensor_data):
    if not sensor_data:
        return None, None
    max_key = max(sensor_data, key=sensor_data.get)
    return max_key, sensor_data[max_key]

if __name__ == '__main__':
    sensor_readings = {
        'temperature_sensor_1': 23.5,
        'humidity_sensor_2': 65.0,
        'pressure_sensor_3': 1013.25,
        'light_sensor_4': 450.0,
        'motion_sensor_5': 0.0
    }
    max_key, max_value = find_max_sensor_reading(sensor_readings)
    print((max_key, max_value))