import math

def celsius_to_kelvin(celsius: float) -> float:
    """Convert temperature from Celsius to Kelvin."""
    return celsius + 273.15

# Predefined set of sensor inputs (hard-coded sample values in Celsius)
SENSOR_DATA = [
    {"id": "S001", "location": "North Hallway", "reading_c": -4.5},
    {"id": "S002", "location": "Server Room A", "reading_c": 38.2},
    {"id": "S003", "location": "Office Lobby", "reading_c": 21.7},
    {"id": "S004", "location": "Warehouse B", "reading_c": -15.3},
    {"id": "S005", "location": "Lab Zone C", "reading_c": 68.9}
]

def format_table(data_list):
    """Print a neatly formatted table of sensor data with Kelvin conversion."""
    print(f"{'ID':<12} {'Location':<24} {'Celsius (°C)':>10} {'Kelvin (K)'>15}")
    print("-" * 65)

    for item in data_list:
        c = item["reading_c"]
        k = celsius_to_kelvin(c)
        
        # Format Celsius with one decimal place, Kelvin with one decimal place
        line = f"{item['id']:<12} {item['location']:<24} {c:>8.1f} {k:9.1f}"
        print(line)

if __name__ == '__main__':
    # Process the predefined data and display results
    format_table(SENSOR_DATA)