import math

def celsius_to_kelvin(celsius: float) -> float:
    """Convert temperature from Celsius to Kelvin."""
    return celsius + 273.15

# Hard-coded sample sensor data (Celsius)
SENSOR_DATA = [
    {"id": "S001", "location": "North Hallway", "reading_celsius": -4.5},
    {"id": "S002", "location": "Server Room A", "reading_celsius": 23.8},
    {"id": "S003", "location": "Lab Window", "reading_celsius": 19.2},
    {"id": "S004", "location": "Parking Garage", "reading_celsius": -7.1},
    {"id": "S005", "location": "Main Lobby", "reading_celsius": 21.6}
]

def format_table(data: list) -> None:
    """Print the temperature data in a formatted table with Celsius and Kelvin values."""
    # Calculate column widths for alignment

if __name__ == '__main__':
    pass
