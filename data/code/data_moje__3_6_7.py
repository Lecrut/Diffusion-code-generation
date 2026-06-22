def celsius_to_kelvin(celsius):
    return celsius + 273.15

def get_temperature_data():
    sensors = {
        "Sensor_A": 25.0,
        "Sensor_B": 100.0,
        "Sensor_C": -40.0,
        "Sensor_D": 0.0,
        "Sensor_E": 37.5
    }
    return sensors

def format_temperature_table(data):
    lines = []
    lines.append(f"{'Sensor':<15} {'Celsius':<15} {'Kelvin':<15}")
    lines.append("-" * 45)
    for sensor_name, celsius_val in data.items():
        kelvin_val = celsius_to_kelvin(celsius_val)
        lines.append(f"{sensor_name:<15} {celsius_val:<15.2f} {kelvin_val:<15.2f}")
    return "\n".join(lines)

if __name__ == '__main__':
    raw_data = get_temperature_data()
    table_output = format_temperature_table(raw_data)
    print(table_output)