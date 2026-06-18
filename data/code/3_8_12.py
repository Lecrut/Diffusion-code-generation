import math

def celsius_to_kelvin(celsius: float) -> float:
    """Convert temperature from Celsius to Kelvin."""
    return celsius + 273.15

# Predefined sensor data sample (hard-coded for no external input dependency)
SENSOR_DATA = [
    {"id": "SEN-001", "celsius": -40},
    {"id": "SEN-002", "celsius": 25},
    {"id": "SEN-003", "celsius": 87.5},
    {"id": "SEN-004", "celsius": -196},
]

def format_temperature_table(data: list) -> None:
    """Display the sensor data in a formatted table with Kelvin conversion."""
    print(f"{'ID':<10} {'Celsius (°C)':>20} {'Kelvin (K)':>35}")
    print("-" * 65)

    for entry in data:
        c_temp = entry["celsius"]
        k_temp = celsius_to_kelvin(c_temp)
        
        # Formatting to align columns nicely

if __name__ == '__main__':
    pass
