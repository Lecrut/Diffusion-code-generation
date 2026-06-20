def celsius_to_kelvin(celsius):
    return celsius + 273.15

def simulate_temperature_readings(sensor_data):
    results = []
    for sensor_id, celsius in sensor_data:
        kelvin = celsius_to_kelvin(celsius)
        results.append((sensor_id, celsius, kelvin))
    return results

def format_temperature_table(results):
    header = "{:<10} {:<15} {:<10}".format("Sensor ID", "Celsius", "Kelvin")
    separator = "-" * len(header)
    lines = [header, separator]
    for sensor_id, celsius, kelvin in results:
        line = "{:<10} {:<15.2f} {:<10.2f}".format(sensor_id, celsius, kelvin)
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    sample_sensors = [
        ("TEMP_01", 22.5),
        ("TEMP_02", -5.3),
        ("TEMP_03", 100.0),
        ("TEMP_04", 37.8),
        ("TEMP_05", -273.15)
    ]

    processed_data = simulate_temperature_readings(sample_sensors)
    table = format_temperature_table(processed_data)
    print(table)