import math

class Sensor:
    """Handles reading raw temperature data from a sensor."""
    
    def __init__(self, device_id):
        self.device_id = device_id
    
    def read_raw_temperature(self) -> float:
        """Simulates reading the raw temperature value in Celsius.
        
        Returns:
            float: The raw temperature reading in degrees Celsius.
        """
        # Simulating a hardware sensor reading with some noise
        base_temp = 25.0
        random_noise = (math.random() - 0.5) * 1.0
        return round(base_temp + random_noise, 3)

class Converter:
    """Handles all necessary unit conversions for temperature data."""
    
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """Converts Celsius to Fahrenheit.
        
        Args:
            celsius (float): Temperature in degrees Celsius.
            
        Returns:
            float: Temperature in degrees Fahrenheit.
        """
        return round((celsius * 9/5) + 32, 2)

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        """Converts Fahrenheit to Celsius.
        
        Args:
            fahrenheit (float): Temperature in degrees Fahrenheit.
            
        Returns:
            float: Temperature in degrees Celsius.
        """
        return round((fahrenheit - 32) * 5/9, 2)

    @staticmethod
    def celsius_to_kelvin(celsius: float) -> float:
        """Converts Celsius to Kelvin.
        
        Args:
            celsius (float): Temperature in degrees Celsius.
            
        Returns:
            float: Temperature in Kelvin.
        """
        return round(celsius + 273.15, 2)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    sensor = Sensor(device_id="TEMP-001")
    
    print(f"Reading raw data from device {sensor.device_id}...")
    raw_temp_celsius = sensor.read_raw_temperature()
    
    converter = Converter()
    
    # Perform conversions using the separated logic
    temp_fahrenheit = converter.celsius_to_fahrenheit(raw_temp_celsius)
    temp_kelvin = converter.celsius_to_kelvin(raw_temp_celsius)
    
    print(f"Raw Temperature (C): {raw_temp_celsius}")
    print(f"Converted to Fahrenheit: {temp_fahrenheit}°F")
    print(f"Converted to Kelvin: {temp_kelvin}K")