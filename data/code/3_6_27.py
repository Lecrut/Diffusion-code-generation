def celsius_to_kelvin(celsius):
    return celsius + 273.15

def format_temperature_data(sensor_data):
    header = f"{'Sensor ID':<10} {'Celsius':>10} {'Kelvin':>10}"
    print(header)
    print("-" * (len(header)))
    for sensor_id, celsius in sensor_data.items():
        kelvin = celsius_to_kelvin(celsius)
        print(f"{sensor_id:<10} {celsius:>10.2f} {kelvin:>10.2f}")

if __name__ == '__main__':
    sample_sensor_data = {
        'S001': 25.3,
        'S002': -4.8,
        'S003': 0.0,
        'S004': 100.0
    }
    format_temperature_data(sample_sensor_data)