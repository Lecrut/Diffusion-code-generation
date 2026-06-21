def celsius_to_kelvin(celsius):
    return celsius + 273.15

def display_temperature_data(sensor_data):
    print(f"{'Sensor ID':<10} {'Celsius':<10} {'Kelvin':<10}")
    for sensor_id, temperature in sensor_data.items():
        kelvin = celsius_to_kelvin(temperature)
        print(f"{sensor_id:<10} {temperature:<10.2f} {kelvin:<10.2f}")

if __name__ == '__main__':
    sample_sensor_data = {
        'Sensor001': 25.3,
        'Sensor002': -5.0,
        'Sensor003': 0.0,
        'Sensor004': 100.0
    }
    display_temperature_data(sample_sensor_data)