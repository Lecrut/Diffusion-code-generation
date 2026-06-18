class TemperatureConverter:
    """A class to convert temperature values between Celsius and Fahrenheit."""
    
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """
        Converts a temperature value from degrees Celsius to degrees Fahrenheit.
        
        The conversion formula used is F = (C * 9/5) + 32.
        
        Args:
            celsius (float): The temperature in degrees Celsius.
            
        Returns:
            float: The equivalent temperature in degrees Fahrenheit.
        """
        return (celsius * 9 / 5) + 32

if __name__ == '__main__':
    # Sample conversions without user input or external dependencies
    
    converter = TemperatureConverter()
    
    # Test cases with hard-coded values
    test_cases = [0, 10.5, -40, 100]
    
    print("Celsius to Fahrenheit Conversion Results:")
    for c_temp in test_cases:
        f_temp = converter.celsius_to_fahrenheit(c_temp)
        print(f"{c_temp}°C is equal to {f_temp:.2f}°F")