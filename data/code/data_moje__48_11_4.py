def find_max_sensor_reading():
    sensor_readings = {
        "temperature": 23.5,
        "humidity": 60.2,
        "pressure": 1013.25,
        "light": 450.0,
        "sound": 55.8,
        "wind_speed": 12.3,
        "co2_level": 415.0,
        "pm25": 35.6
    }
    max_key = None
    max_value = float('-inf')
    for key, value in sensor_readings.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key, max_value

if __name__ == '__main__':
    result = find_max_sensor_reading()
    print(result)