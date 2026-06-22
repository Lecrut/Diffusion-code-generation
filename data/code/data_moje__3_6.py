import math

def convert_to_kelvin(celsius):
    return celsius + 273.15

def format_table(sensor_data):
    header = f"{'Sensor ID':<12} {'Celsius':<10} {'Kelvin':<10}"
    separator = "-" * len(header)
    lines = [header, separator]
    for sensor_id, celsius in sensor_data:
        kelvin = convert_to_kelvin(celsius)
        line = f"{sensor_id:<12} {celsius:<10.2f} {kelvin:<10.2f}"
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    sensor_data = [
        ("S001", 25.5),
        ("S002", -10.0),
        ("S003", 100.0),
        ("S004", 0.0),
    ]
    print(format_table(sensor_data))