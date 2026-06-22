def find_max_sensor_reading():
    sensor_readings = {
        "temperature_01": 23.5,
        "temperature_02": 24.1,
        "humidity_01": 45.2,
        "pressure_01": 1013.25,
        "light_intensity_01": 500.0,
        "vibration_01": 0.05
    }
    
    max_key = None
    max_value = float('-inf')
    
    for key, value in sensor_readings.items():
        if value > max_value:
            max_key = key
            max_value = value
            
    return max_key, max_value

if __name__ == '__main__':
    result_key, result_value = find_max_sensor_reading()
    print((result_key, result_value))