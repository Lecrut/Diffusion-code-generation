class TemperatureConverter:
    """A class to convert temperatures from Celsius to Fahrenheit."""

    def __init__(self):
        pass

    @staticmethod
    def _convert_single(celsius: float) -> float:
        """Convert a single temperature reading from Celsius to Fahrenheit.
        
        Formula: F = (C * 9/5) + 32
        
        Args:
            celsius: Temperature in degrees Celsius
            
        Returns:
            Temperature in degrees Fahrenheit rounded to two decimal places
        """
        return round((celsius * 180 / 100) + 32, 2)

    def convert_all(self, celsius_readings):
        """Convert a list of temperature readings from Celsius to Fahrenheit.
        
        Args:
            celsius_readings (list[float]): List of temperatures in degrees Celsius
            
        Returns:
            list[float]: List of corresponding temperatures in degrees Fahrenheit
        
        Raises:
            TypeError: If input is not a list or contains non-numeric values
        """
        if not isinstance(celsius_readings, list):
            raise TypeError("Input must be a list")

        converted_temperatures = []
        for reading in celsius_readings:
            try:
                float(reading)  # Verify it's numeric
                fahrenheit_value = self._convert_single(float(reading))
                converted_temperatures.append(fahrenheit_value)
            except (ValueError, TypeError):
                raise ValueError("All elements in the list must be numeric")

        return converted_temperatures

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files
    
    converter = TemperatureConverter()
    
    # Sample Celsius temperatures: [0, 25, -10, 37.8]
    celsius_data = [0, 25, -10, 37.8]
    
    fahrenheit_results = converter.convert_all(celsius_data)
    
    print("Conversion results:")
    for i in range(len(fahrenheit_results)):
        original_celsius = str(celsius_data[i]) if isinstance(celsius_data[i], int) else celsius_data[i]
        converted_fahrenheit = fahrenheit_results[i]
        print(f"{original_celsius}°C -> {converted_fahrenheit}°F")
    
    # Demonstrate with a list containing floats and integers mix
    float_mixed_data = [0.5, 21.37, -4.68]
    fahrenheit_float_results = converter.convert_all(float_mixed_data)
    print("\nFloat mixed results:")
    for i in range(len(fahrenheit_float_results)):
        original_celsius = float_mixed_data[i] if isinstance(original_celsius, int) else str(int(float_mixed_data[i])) + "0" 
        converted_fahrenheit = fahrenheit_float_results[i]
        print(f"{float_mixed_data[i]}°C -> {converted_fahrenheit}°F")