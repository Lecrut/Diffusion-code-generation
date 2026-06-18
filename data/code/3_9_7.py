import math

class Sensor:
    """Handles reading raw temperature data from a sensor."""
    
    def __init__(self, device_id):
        self.device_id = device_id
    
    def read_raw_temperature(self):
        """Simulates reading raw temperature data in Fahrenheit.
        
        Returns:
            float: Raw temperature value in degrees Fahrenheit.
        """
        # Simulating a sensor reading with some noise around 72°F
        return round(71.5 + (math.random() - 0.5) * 0.4, 2)

class Converter:
    """Handles all necessary unit conversions for temperature data."""
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        """Converts Fahrenheit to Celsius using the formula C = (F - 32) / 1.8
        
        Args:
            fahrenheit (float): Temperature in degrees Fahrenheit
            
        Returns:
            float: Temperature in degrees Celsius
        """
        return round((fahrenheit - 32) * 5/9, 2)

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Converts Celsius to Fahrenheit using the formula F = C * 1.8 + 32
        
        Args:
            celsius (float): Temperature in degrees Celsius
            
        Returns:
            float: Temperature in degrees Fahrenheit
        """
        return round(celsius * 9/5 + 32, 2)

    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit):
        """Converts Fahrenheit to Kelvin using the formula K = (F - 32) / 1.8 + 273.15
        
        Args:
            fahrenheit (float): Temperature in degrees Fahrenheit
            
        Returns:
            float: Temperature in Kelvin
        """
        return round((fahrenheit - 32) * 5/9 + 273.15, 4)

if __name__ == '__main__':
    # Initialize sensor with a mock device ID
    my_sensor = Sensor(device_id="TEMP-001")

    # Read raw temperature data (simulated as Fahrenheit)
    raw_temp_fahrenheit = my_sensor.read_raw_temperature()
    
    print(f"Raw Temperature ({my_sensor.device_id}): {raw_temp_fahrenheit} °F")

    # Create converter instance to perform conversions
    temp_converter = Converter()

    # Convert to Celsius
    celsius_value = temp_converter.fahrenheit_to_celsius(raw_temp_fahrenheit)
    print(f"Celsius: {celsius_value} °C")

    # Convert to Kelvin
    kelvin_value = temp_converter.fahrenheit_to_kelvin(raw_temp_fahrenheit)
    print(f"Kelvin: {kelvin_value} K")