def find_max_sensor_reading():
    sensor_readings = {
        "sensor_1": 15.2,
        "sensor_2": 30.5,
        "sensor_3": 22.1,
        "sensor_4": 45.9,
        "sensor_5": 10.0
    }
    max_key = None
    max_value = None
    for key, value in sensor_readings.items():
        if max_key is None or value > max_value:
            max_key = key
            max_value = value
    return (max_key, max_value)

if __name__ == '__main__':
    result = find_max_sensor_reading()
    print(result)