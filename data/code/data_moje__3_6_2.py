def convert_celsius_to_kelvin(celsius):
    return celsius + 273.15

def format_temperature_table(temperatures_celsius):
    header = f"{'Sensor':<10} {'Celsius':>10} {'Kelvin':>10}"
    separator = "-" * len(header)
    lines = [header, separator]
    for i, celsius in enumerate(temperatures_celsius, 1):
        kelvin = convert_celsius_to_kelvin(celsius)
        row = f"{f'Sensor {i}':<10} {celsius:>10.2f} {kelvin:>10.2f}"
        lines.append(row)
    return "\n".join(lines)

if __name__ == '__main__':
    sample_temperatures = [25.5, 30.0, -10.2, 100.0, 0.0]
    result_table = format_temperature_table(sample_temperatures)
    print(result_table)