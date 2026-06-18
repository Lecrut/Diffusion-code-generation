class Sensor:
    """Handles reading raw temperature data from a simulated source."""
    
    def __init__(self, sensor_id: str):
        self.sensor_id = sensor_id
    
    def read_raw_temperature(self) -> float:
        """Simulates reading raw temperature data. 
        Returns the value in Celsius as it is the standard scientific unit for raw output simulation here.
        
        Returns:
            float: The raw temperature reading in degrees Celsius.
        """
        # Simulated hardware returning a specific value to demonstrate functionality without I/O dependencies
        return 25.0

class Converter:
    """Handles all necessary unit conversions, ensuring clean separation of concerns."""
    
    def __init__(self):
        pass
    
    def celsius_to_fahrenheit(self, celsius: float) -> float:
        """Converts temperature from Celsius to Fahrenheit using the formula F = (C * 1.8) + 32.

        Args:
            celsius (float): Temperature in degrees Celsius.

        Returns:
            float: Temperature in degrees Fahrenheit.
        """
        return (celsius * 9 / 5) + 32
    
    def fahrenheit_to_celsius(self, fahrenheit: float) -> float:
        """Converts temperature from Fahrenheit to Celsius using the formula C = (F - 32) / 1.8

        Args:
            fahrenheit (float): Temperature in degrees Fahrenheit.

        Returns:
            float: Temperature in degrees Celsius.
        """
        return (fahrenheit - 32) * 5 / 9
    
    def celsius_to_kelvin(self, celsius: float) -> float:
        """Converts temperature from Celsius to Kelvin using the formula K = C + 273.15

        Args:
            celsius (float): Temperature in degrees Celsius.

        Returns:
            float: Temperature in Kelvin.
        """
        return celsius + 273.15
    
    def kelvin_to_celsius(self, kelvin: float) -> float:
        """Converts temperature from Kelvin to Celsius using the formula C = K - 273.15

        Args:
            kelvin (float): Temperature in Kelvin.

        Returns:
            float: Temperature in degrees Celsius.
        """
        return kelvin - 273.15

if __name__ == '__main__':
    # Initialize components with hard-coded sample values to ensure the module runs without input or files
    
    sensor = Sensor("TEMP_001")
    
    # Read raw data (assumed Celsius)
    raw_temp_celsius = sensor.read_raw_temperature()
    
    print(f"Raw Temperature ({sensor.sensor_id}): {raw_temp_celsius}°C")
    
    converter = Converter()
    
    # Demonstrate conversion capabilities using the separated logic
    
    fahrenheit_result = converter.celsius_to_fahrenheit(raw_temp_celsius)
    kelvin_result = converter.celsius_to_kelvin(raw_temp_celsius)
    
    print(f"Converted to Fahrenheit: {fahrenheit_result}°F")
    print(f"Converted to Kelvin: {kelvin_result:.2f} K")
    
    # Verify reverse conversion accuracy
    
    back_to_cels_from_f = converter.fahrenheit_to_celsius(fahrenheit_result)
    back_to_kelvin_from_k = converter.kelvin_to_celsius(kelvin_result)
    
    print(f"Reverse check (F->C): {back_to_cels_from_f}°C")
    print(f"Reverse check (K->C): {back_to_kelvin_from_k:.2f}°C")