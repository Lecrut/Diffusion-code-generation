def celsius_to_kelvin(celsius):
    return celsius + 273.15

def validate_sensor_data(sensor_data):
    if not isinstance(sensor_data, dict):
        raise ValueError("Sensor data must be a dictionary")
    for sensor_id, temp_c in sensor_data.items():
        if not isinstance(sensor_id, str) or not isinstance(temp_c, (int, float)):
            raise ValueError("Invalid sensor ID or temperature value")

def display_temperature_data(sensor_data):
    validate_sensor_data(sensor_data)
    print(f"{'Sensor ID':<10} {'Celsius':<10} {'Kelvin':<10}")
    for sensor_id, temp_c in sensor_data.items():
        temp_k = celsius_to_kelvin(temp_c)
        print(f"{sensor_id:<10} {temp_c:<10.2f} {temp_k:<10.2f}")

if __name__ == '__main__':
    sample_sensor_data = {
        'SensorA': 30.5,
        'SensorB': -10.0,
        'SensorC': 50.0,
        'SensorD': 20.0
    }
    display_temperature_data(sample_sensor_data)