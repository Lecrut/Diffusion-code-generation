def simulate_temperature_readings(sensor_data):
    results = []
    for sensor_id, celsius in sensor_data:
        kelvin = celsius + 273.15
        results.append({
            "sensor_id": sensor_id,
            "celsius": celsius,
            "kelvin": kelvin
        })
    return results

def format_table(results):
    header = f"{'Sensor ID':<12} {'Celsius (°C)':<15} {'Kelvin (K)':<15}"
    separator = "-" * len(header)
    lines = [header, separator]
    for entry in results:
        line = f"{entry['sensor_id']:<12} {entry['celsius']:<15.2f} {entry['kelvin']:<15.2f}"
        lines.append(line)
    return "\n".join(lines)

if __name__ == "__main__":
    sample_sensors = [
        ("TH-001", 22.5),
        ("TH-002", 18.3),
        ("TH-003", 25.7),
        ("TH-004", -5.2),
        ("TH-005", 30.0)
    ]
    processed_data = simulate_temperature_readings(sample_sensors)
    table_output = format_table(processed_data)
    print(table_output)