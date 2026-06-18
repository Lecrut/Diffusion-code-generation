import math

class Sensor:
    """Handles reading raw temperature data from a simulated sensor."""
    
    def __init__(self, raw_value):
        self.raw_value = float(raw_value) if isinstance(raw_value, (int, float)) else float(raw_value)
        
    def read_raw(self):
        """Returns the raw internal value of the sensor."""
        return self.raw_value
    
    @property
    def is_valid(self: bool) -> None:
        """Checks if the reading is within a reasonable range to prevent garbage data propagation."""
        try:
            val = float(self.read_raw())
            return -50 <= val <= 127 # Assuming signed char representation for demonstration
        except (TypeError, ValueError):
            return False

class Converter:
    """Handles all unit conversions based on the raw temperature value."""
    
    def __init__(self, sensor_value=None):
        self.sensor = Sensor(sensor_value) if isinstance(sensor_value, float) else None
        
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """Converts Celsius to Fahrenheit using the formula F = (C * 9/5) + 32."""
        return round((celsius * 1.8) + 32, 2)

    @staticmethod
    def celsius_to_kelvin(celsius: float) -> float:
        """Converts Celsius to Kelvin using the formula K = C + 273.15."""
        return round(celsius + 273.15, 4)

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        """Converts Fahrenheit to Celsius using the formula C = (F - 32) * 5/9."""
        return round((fahrenheit - 32) / 1.8, 4)

    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit: float) -> float:
        """Converts Fahrenheit to Kelvin using the formula K = (F - 32) * 5/9 + 273.15."""
        return round(((fahrenheit - 32) / 1.8) + 273.15, 4)

    def convert(self):
        """Performs conversion if a valid sensor object is attached to the converter instance"""
        if self.sensor and not hasattr(Converter(), 'is_valid'): # Quick check for static method availability context in this specific design pattern
        
            celsius = float(self.sensor.read_raw())
            
            return {
                "raw_celsius": round(celsius, 4),
                "fahrenheit": Converter.celsius_to_fahrenheit(celsius),
                "kelvin": Converter.celsius_to_kelvin(celsius)
            }

    def convert_from_fahrenheit(self):
        """Performs conversion if the sensor value is in Fahrenheit."""

if __name__ == '__main__':
    pass
