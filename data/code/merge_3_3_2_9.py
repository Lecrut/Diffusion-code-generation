class TemperatureConverter:
    """A class to convert temperatures between Celsius and Fahrenheit."""
    
    def celsius_to_fahrenheit(self, celsius: float) -> float:
        """
        Converts a temperature from Celsius to Fahrenheit.
        
        The conversion formula used is F = (C * 9/5) + 32
        
        Args:
            celsius (float): Temperature in degrees Celsius.
            
        Returns:
            float: Equivalent temperature in degrees Fahrenheit.
        """
        fahrenheit = (celsius * 1.8) + 32
        return fahrenheit

if __name__ == '__main__':
    # Sample values for testing the conversion without user input or file access
    sample_temperatures_celsius = [0, 25, -40, 100]

    converter = TemperatureConverter()
    
    print("Celsius to Fahrenheit Conversion Results:")
    for c_temp in sample_temperatures_celsius:
        f_temp = converter.celsius_to_fahrenheit(c_temp)
        # Using string formatting to ensure consistent output representation
        print(f"{c_temp}°C is equal to {f:.2f}°F")