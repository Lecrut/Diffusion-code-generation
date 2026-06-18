import math

def celsius_to_kelvin(celsius: float) -> float:
    """Convert temperature from Celsius to Kelvin."""
    return celsius + 273.15

class TemperatureDataProcessor:
    def __init__(self):
        self.sensor_data = []

    def add_entry(self, sensor_id: str, reading_celsius: float) -> None:
        """Add a temperature entry to the internal list."""
        kelvin_temp = celsius_to_kelvin(reading_celsius)
        self.sensor_data.append({
            'sensor_id': sensor_id,
            'celsius': round(reading_celsius, 2),
            'kelvin': round(kelvin_temp, 2)
        })

    def display_table(self) -> None:
        """Display the temperature data in a formatted table."""
        if not self.sensor_data:
            print("No sensor data available.")
            return

        # Calculate column widths for neat formatting

if __name__ == '__main__':
    pass
