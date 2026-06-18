import math

class Sensor:
    """Handles reading raw temperature data."""
    
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
    
    def read_raw_temperature(self):
        """Simulates reading a raw temperature value in Fahrenheit.
        
        Returns:
            float: The raw temperature value (Fahrenheit).
        """
        # Simulated raw data logic
        return 98.6

class Converter:
    """Handles all necessary unit conversions."""
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        """Converts a temperature from Fahrenheit to Celsius.
        
        Args:
            fahrenheit (float): Temperature in Fahrenheit.
            
        Returns:
            float: Temperature in Celsius.
        """
        return (fahrenheit - 32) * 5 / 9
    
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Converts a temperature from Celsius to Fahrenheit.
        
        Args:
            celsius (float): Temperature in Celsius.
            
        Returns:
            float: Temperature in Fahrenheit.
        """
        return (celsius * 9 / 5) + 32
    
    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit):
        """Converts a temperature from Fahrenheit to Kelvin.
        
        Args:
            fahrenheit (float): Temperature in Fahrenheit.
            
        Returns:
            float: Temperature in Kelvin.
        """
        celsius = Converter.fahrenheit_to_celsius(fahrenheit)
        return celsius + 273.15

def main():
    # Hard-coded sample values as per task requirements (no user input)
    sensor_id = "TEMP_001"
    
    # Instantiate Sensor and Converter classes
    my_sensor = Sensor(sensor_id)
    temp_converter = Converter()
    
    try:
        raw_temp_fahrenheit = my_sensor.read_raw_temperature()
        
        if not isinstance(raw_temp_fahrenheit, (int, float)):
            raise ValueError("Invalid temperature reading")
            
        # Perform conversions using the Converter class
        celsius_temp = temp_converter.fahrenheit_to_celsius(raw_temp_fahrenheit)
        kelvin_temp = temp_converter.fahrenheit_to_kelvin(raw_temp_fahrenheit)
        
        print(f"Sensor ID: {sensor_id}")
        print(f"Raw Temperature (°F): {raw_temp_fahrenheit:.2f}")
        print(f"Converted Temperature (°C): {celsius_temp:.2f}")
        print(f"Converted Temperature (K): {kelvin_temp:.2f}")
        
    except Exception as e:
        print(f"Error during processing: {e}")

if __name__ == '__main__':
    main()