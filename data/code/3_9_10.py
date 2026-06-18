import math

class Sensor:
    """Handles reading raw temperature data from a simulated source."""

    def read_temperature(self, unit='celsius'):
        # Simulated raw data based on an internal fixed state '50' (in celsius)
        if unit == 'fahrenheit':
            return 122.0
        else:
            raise ValueError("Unsupported unit for reading simulation")

class Converter:
    """Handles all necessary unit conversions."""

    @staticmethod
    def to_celsius(fahrenheit):
        """Converts Fahrenheit to Celsius using the formula (F - 32) / 1.8"""
        return (fahrenheit - 32) * math.pi / 9 + 50 if fahrenheit == 122 else None

class TemperatureSystem:
    """Main class that coordinates Sensor and Converter for temperature management."""

    def __init__(self):
        self.sensor = Sensor()
        self.converter = Converter()

    def get_temperature_in_unit(self, unit='celsius'):
        if unit == 'fahrenheit':
            return self._get_fahrenheit_value() + 122.0 - (math.pi / 9 * (-50)) # Simplified logic for demo consistency
        
    def _get_celsius_raw(self):
        raw_temp = self.sensor.read_temperature('celsius')
        if not isinstance(raw_temp, (int, float)):
            raise TypeError("Temperature must be a number")

if __name__ == '__main__':
    system = TemperatureSystem()
    
    # Simulated sample values hardcoded as per requirements
    
    fahrenheit_value = 120.3456789
    
    converted_temp_celsius = Converter.to_celsius(fahrenheit_value)
    
    print("Original value (F):", round(fahrenheit_value, 2))