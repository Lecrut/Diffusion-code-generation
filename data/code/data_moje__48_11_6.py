def find_max_sensor_reading(sensor_readings):
    max_key = max(sensor_readings, key=sensor_readings.get)
    return max_key, sensor_readings[max_key]

if __name__ == '__main__':
    sensor_readings = {
        'temperature': 23.5,
        'humidity': 60.2,
        'pressure': 1013.25,
        'wind_speed': 15.8,
        'light_intensity': 450.0
    }
    key, value = find_max_sensor_reading(sensor_readings)
    print((key, value))