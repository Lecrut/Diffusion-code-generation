def simulate_temperature_readings():
    sensors = [
        {"id": "S001", "name": "Living Room", "celsius": 22.5},
        {"id": "S002", "name": "Kitchen", "celsius": 24.0},
        {"id": "S003", "name": "Bedroom", "celsius": 19.5},
        {"id": "S004", "name": "Garage", "celsius": 15.0},
        {"id": "S005", "name": "Server Room", "celsius": 18.0}
    ]
    
    results = []
    for sensor in sensors:
        kelvin = sensor["celsius"] + 273.15
        results.append({
            "id": sensor["id"],
            "name": sensor["name"],
            "celsius": sensor["celsius"],
            "kelvin": round(kelvin, 2)
        })
    
    return results

def format_temperature_table(readings):
    if not readings:
        return ""
    
    header = f"{'Sensor ID':<12} {'Location':<15} {'Celsius':>10} {'Kelvin':>10}"
    separator = "-" * len(header)
    
    lines = [header, separator]
    
    for reading in readings:
        line = f"{reading['id']:<12} {reading['name']:<15} {reading['celsius']:>10.2f} {reading['kelvin']:>10.2f}"
        lines.append(line)
    
    return "\n".join(lines)

if __name__ == '__main__':
    readings = simulate_temperature_readings()
    table = format_temperature_table(readings)
    print(table)