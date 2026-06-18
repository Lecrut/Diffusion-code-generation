"""
Temperature Data Processing Module

This module demonstrates an object-oriented approach to handling temperature data.
It separates concerns between reading raw sensor data (Sensor class) 
and performing unit conversions (Converter class).
"""

class Sensor:
    """Handles reading raw temperature data from a simulated source."""

    def __init__(self, device_id: str):
        self.device_id = device_id
    
    @staticmethod
    def _simulate_raw_read() -> float:
        """Simulates the internal sensor read operation. 
        Returns a value in Celsius as per standard SI units for temperature sensors.
        
        Note: In a real-world scenario, this would call hardware APIs or file I/O."""
        # Simulated raw reading result (Celsius)
        return 25.0

class Converter:
    """Handles unit conversions between different temperature scales."""

    @staticmethod
    def to_fahrenheit(celsius_value: float) -> float:
        """Converts a temperature value from Celsius to Fahrenheit."""
        return celsius_value * 9 / 5 + 32.0

    @staticmethod
    def to_kelvin(celsius_value: float) -> float:
        """Converts a temperature value from Celsius to Kelvin."""
        return celsius_value + 273.15

def main():
    # Hard-coded sample values as per requirements (no user input, args, or files needed)

    # Instantiate the sensor with a mock device ID
    my_sensor = Sensor("TEMP_001")

    # Read raw data directly from the sensor object
    celsius_data = my_sensor._simulate_raw_read()

    print(f"Raw Temperature Data (Celsius): {celsius_data:.2f} °C")

    # Use the Converter class to perform unit conversions
    fahrenheit_value = Converter.to_fahrenheit(celsius_data)
    kelvin_value = Converter.to_kelvin(celsius_data)

    print(f"Converted Value (Fahrenheit): {fahrenheit_value:.2f} °F")
    print(f"Converted Value (Kelvin): {kelvin_value:.2f} K")

if __name__ == '__main__':
    main()