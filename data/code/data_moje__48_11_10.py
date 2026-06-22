def find_max_sensor_reading(sensor_data):
    if not sensor_data:
        return None
    max_key = max(sensor_data, key=sensor_data.get)
    return max_key, sensor_data[max_key]

if __name__ == '__main__':
    sensor_readings = {
        'temperature': 23.5,
        'humidity': 60.2,
        'pressure': 1013.25,
        'light_intensity': 500,
        'wind_speed': 15.7
    }
    result = find_max_sensor_reading(sensor_readings)
    print(result)