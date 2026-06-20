def convert_celsius_to_kelvin(temperature_celsius):
    return temperature_celsius + 273.15

def process_temperature_data(temperatures_celsius):
    results = []
    for temp in temperatures_celsius:
        kelvin = convert_celsius_to_kelvin(temp)
        results.append({"celsius": temp, "kelvin": kelvin})
    return results

def format_temperature_table(data):
    header = f"{'Sensor':<10} {'Celsius':<10} {'Kelvin':<10}"
    separator = "-" * 30
    lines = [header, separator]
    for index, entry in enumerate(data):
        sensor_id = f"Sensor_{index + 1}"
        line = f"{sensor_id:<10} {entry['celsius']:<10.2f} {entry['kelvin']:<10.2f}"
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    sample_temperatures = [20.5, 25.0, -5.3, 37.0, 0.0, 100.0]
    processed_data = process_temperature_data(sample_temperatures)
    formatted_table = format_temperature_table(processed_data)
    print(formatted_table)