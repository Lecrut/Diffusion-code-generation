def celsius_to_kelvin(celsius):
    return celsius + 273.15

def format_temperature_table(sensor_data):
    header = f"{'Sensor ID':<12} {'Temp (°C)':<12} {'Temp (K)':<12}"
    separator = "-" * len(header)
    lines = [header, separator]
    for sensor_id, celsius in sensor_data:
        kelvin = celsius_to_kelvin(celsius)
        row = f"{sensor_id:<12} {celsius:<12.2f} {kelvin:<12.2f}"
        lines.append(row)
    return "\n".join(lines)

if __name__ == '__main__':
    sample_sensors = [
        ("Sensor_01", 22.5),
        ("Sensor_02", 30.0),
        ("Sensor_03", -5.2),
        ("Sensor_04", 100.0),
        ("Sensor_05", 0.0),
    ]
    table = format_temperature_table(sample_sensors)
    print(table)