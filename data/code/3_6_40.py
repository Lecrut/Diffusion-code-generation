def convert_to_kelvin(celsius):
    return celsius + 273.15

def display_temperatures(sensor_data):
    print(f"{'Sensor ID':<10} {'Celsius':<10} {'Kelvin':<10}")
    for sensor_id, temp_celsius in sensor_data.items():
        temp_kelvin = convert_to_kelvin(temp_celsius)
        print(f"{sensor_id:<10} {temp_celsius:<10.2f} {temp_kelvin:<10.2f}")

if __name__ == '__main__':
    sample_sensor_data = {
        'Sensor001': 25.3,
        'Sensor002': -5.0,
        'Sensor003': 100.0
    }
    display_temperatures(sample_sensor_data)