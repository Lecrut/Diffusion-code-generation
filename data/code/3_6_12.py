import math

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def format_temperature_table(sensor_data):
    header = f"{'Sensor':<15} {'Celsius':>10} {'Kelvin':>10}"
    separator = "-" * len(header)
    rows = [header, separator]
    
    for name, celsius in sensor_data:
        kelvin = celsius_to_kelvin(celsius)
        row = f"{name:<15} {celsius:>10.2f} {kelvin:>10.2f}"
        rows.append(row)
    
    return "\n".join(rows)

if __name__ == '__main__':
    sensors = [
        ("Ambient", 25.0),
        ("Engine", 95.5),
        ("Coolant", 80.0),
        ("Exhaust", 450.0)
    ]
    
    result = format_temperature_table(sensors)
    print(result)