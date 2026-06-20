def celsius_to_kelvin(celsius):
    return celsius + 273.15

def format_temperature_table(sensor_data):
    header = f"{'Sensor ID':<10} {'Temp (°C)':<12} {'Temp (K)':<12}"
    separator = "-" * len(header)
    lines = [header, separator]
    for sensor_id, temp_c in sensor_data:
        temp_k = celsius_to_kelvin(temp_c)
        line = f"{str(sensor_id):<10} {temp_c:<12.2f} {temp_k:<12.2f}"
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    sample_sensor_data = [
        (1, 20.5),
        (2, -5.0),
        (3, 36.6),
        (4, 100.0),
        (5, -273.15)
    ]
    table = format_temperature_table(sample_sensor_data)
    print(table)