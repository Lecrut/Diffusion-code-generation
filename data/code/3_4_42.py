def celsius_to_kelvin(celsius):
    return celsius + 273.15

def display_temperature_data(sensor_data):
    header = f"{'Sensor ID':<10} {'Celsius':<10} {'Kelvin':<10}"
    print(header)
    print('-' * len(header))
    for sensor_id, temp_c in sensor_data.items():
        temp_k = celsius_to_kelvin(temp_c)
        print(f"{sensor_id:<10} {temp_c:<10.2f} {temp_k:<10.2f}")

if __name__ == '__main__':
    sample_sensor_data = {
        'SensorA': 37.5,
        'SensorB': -10.0,
        'SensorC': 45.0,
        'SensorD': 20.0
    }
    display_temperature_data(sample_sensor_data)