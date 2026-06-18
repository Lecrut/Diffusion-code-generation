import math

class Sensor:
    """Handles reading raw temperature data from a simulated source."""
    
    def __init__(self):
        self._raw_data = None
    
    def read_raw_temperature(self, value_celsius):
        """Simulates reading a raw temperature in Celsius.
        
        Args:
            value_celsius (float): The temperature value to record as if it was 
                                  just read from a sensor.
        """
        self._raw_data = value_celsius
    
    def get_raw_temperature(self) -> float | None:
        """Returns the last recorded raw temperature in Celsius."""
        return self._raw_data

class Converter:
    """Handles all unit conversions for temperature data to ensure clean separation of concerns."""
    
    @staticmethod
    def celsius_to_fahrenheit(celsius_value: float) -> float:
        """Converts a temperature from Celsius to Fahrenheit.
        
        Formula: F = (C * 9/5) + 32
        
        Args:
            celsius_value (float): Temperature in degrees Celsius.
            
        Returns:
            float: Temperature in degrees Fahrenheit.
        """
        return (celsius_value * 9 / 5) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit_value: float) -> float:
        """Converts a temperature from Fahrenheit to Celsius.
        
        Formula: C = (F - 32) * 5/9
        
        Args:
            fahrenheit_value (float): Temperature in degrees Fahrenheit.
            
        Returns:
            float: Temperature in degrees Celsius.
        """
        return (fahrenheit_value - 32) * 5 / 9
    
    @staticmethod
    def celsius_to_kelvin(celsius_value: float) -> float:
        """Converts a temperature from Celsius to Kelvin.
        
        Formula: K = C + 273.15
        
        Args:
            celsius_value (float): Temperature in degrees Celsius.
            
        Returns:
            float: Temperature in Kelvin.
        """
        return celsius_value + 273.15
    
    @staticmethod
    def kelvin_to_celsius(kelvin_value: float) -> float:
        """Converts a temperature from Kelvin to Celsius.
        
        Formula: C = K - 273.15
        
        Args:
            kelvin_value (float): Temperature in Kelvin.
            
        Returns:
            float: Temperature in degrees Celsius.
        """
        return kelvin_value - 273.15

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    sensor = Sensor()
    
    # Simulate reading raw data (Celsius)
    celsius_reading = 20.0
    fahrenheit_reading = 78.6
    kelvin_reading = 293.15
    
    print("--- Temperature Conversion Demo ---")
    
    # Test Reading Raw Data
    sensor.read_raw_temperature(celsius_reading)
    raw_temp = sensor.get_raw_temperature()
    assert abs(raw_temp - celsius_reading) < 0.01, "Raw data reading failed"
    print(f"Simulated Sensor Read: {raw_temp} °C")
    
    # Test Conversions using Converter class
    
    # Celsius to Fahrenheit
    fahrenheit = Converter.celsius_to_fahrenheit(celsius_reading)