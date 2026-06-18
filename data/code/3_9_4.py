import math

class Sensor:
    """Handles reading raw temperature data from a sensor."""
    
    def __init__(self, device_id):
        self.device_id = device_id
    
    def read_raw(self) -> float:
        """Simulates reading raw temperature data in Celsius.
        
        Returns:
            float: The raw temperature value in degrees Celsius.
        """
        # Simulated sensor returning a fixed hard-coded value for demonstration
        return 25.0

class Converter:
    """Handles unit conversions between different temperature scales."""
    
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """Converts temperature from Celsius to Fahrenheit.
        
        Args:
            celsius (float): Temperature in degrees Celsius.
            
        Returns:
            float: Temperature in degrees Fahrenheit.
        """
        return (celsius * 9 / 5) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        """Converts temperature from Fahrenheit to Celsius.
        
        Args:
            fahrenheit (float): Temperature in degrees Fahrenheit.
            
        Returns:
            float: Temperature in degrees Celsius.
        """
        return (fahrenheit - 32) * 5 / 9
    
    @staticmethod
    def celsius_to_kelvin(celsius: float) -> float:
        """Converts temperature from Celsius to Kelvin.
        
        Args:
            celsius (float): Temperature in degrees Celsius.
            
        Returns:
            float: Temperature in Kelvins.
        """
        return celsius + 273.15
    
    @staticmethod
    def kelvin_to_celsius(kelvin: float) -> float:
        """Converts temperature from Kelvin to Celsius.
        
        Args:
            kelvin (float): Temperature in Kelvins.
            
        Returns:
            float: Temperature in degrees Celsius.
        """
        return kelvin - 273.15

def main():
    # Initialize sensor and converter instances with hard-coded sample values logic
    sensor = Sensor("TEMP-001")
    
    raw_celsius = sensor.read_raw()
    
    print(f"Raw temperature read from {sensor.device_id}: {raw_celsius:.2f} °C")
    
    # Perform conversions using the Converter class
    fahrenheit_value = Converter.celsius_to_fahrenheit(raw_celsius)
    kelvin_value = Converter.celsius_to_kelvin(raw_celsius)
    
    print(f"Converted to Fahrenheit: {fahrenheit_value:.2f} °F")
    print(f"Converted to Kelvin: {kelvin_value:.2f} K")

if __name__ == '__main__':
    main()