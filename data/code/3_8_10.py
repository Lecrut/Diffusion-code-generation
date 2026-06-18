import math

def celsius_to_kelvin(celsius: float) -> float:
    """Convert temperature from Celsius to Kelvin."""
    return celsius + 273.15

def read_sensor_data():
    """Simulate reading predefined sensor data without user input."""
    # Hard-coded sample temperatures in Celsius
    raw_temps = [20.5, -4.2, 87.9, -250.5]  # Includes an unrealistic value to test handling

    return [{"id": i+1, "celsius": temp} for i, temp in enumerate(raw_temps)]

def format_table(data):
    """Generate a formatted table with Celsius and Kelvin values."""
    header = "| ID | Temperature (°C) | Temperature (K) |\n" + "-" * 60
    
    rows = []
    for item in data:
        celsius = round(item["celsius"], 2)
        kelvin = round(celsius_to_kelvin(celsius), 2)
        row = f"| {item['id']} | {celsius:>18} | {kelvin:>19.0f} |\n"
        rows.append(row)

    table_content = header + "\n".join(rows)
    return table_content

if __name__ == '__main__':
    # Simulate sensor input and formatting results
    data_entries = read_sensor_data()
    
    print("Sensor Temperature Data Report")
    print("=" * 60)