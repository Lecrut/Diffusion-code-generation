def find_max_sensor_reading(sensor_data):
    max_key = None
    max_value = None
    for key, value in sensor_data.items():
        if max_value is None or value > max_value:
            max_value = value
            max_key = key
    return max_key, max_value

if __name__ == '__main__':
    sensors = {
        "temp_1": 23.5,
        "temp_2": 45.2,
        "humidity_1": 60.1,
        "pressure_1": 1013.25,
        "wind_speed_1": 12.8
    }
    key, value = find_max_sensor_reading(sensors)
    print(key, value)