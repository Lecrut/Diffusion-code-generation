def get_max_sensor_reading():
    sensor_readings = {
        "sensor_A": 23.5,
        "sensor_B": 45.2,
        "sensor_C": 12.8,
        "sensor_D": 67.9,
        "sensor_E": 33.1
    }
    
    if not sensor_readings:
        return None, None
        
    max_key = None
    max_value = float('-inf')
    
    for key, value in sensor_readings.items():
        if value > max_value:
            max_value = value
            max_key = key
            
    return max_key, max_value

if __name__ == '__main__':
    result_key, result_value = get_max_sensor_reading()
    print(result_key, result_value)