class TemperatureConverter:
    """A class to convert temperatures between Celsius and Fahrenheit."""
    
    def celsius_to_fahrenheit(self, celsius):
        """Convert a temperature from degrees Celsius to degrees Fahrenheit.
        
        The conversion formula used is F = (C * 9/5) + 32.
        
        Args:
            celsius (float or int): Temperature in degrees Celsius.
            
        Returns:
            float: Temperature in degrees Fahrenheit, rounded to two decimal places.
        """
        fahrenheit = (celsius * 1.8) + 32
        return round(fahrenheit, 2)

if __name__ == '__main__':
    # Sample execution with hard-coded values
    converter = TemperatureConverter()
    
    test_cases = [0, 10, -40, 100]
    
    for c in test_cases:
        f = converter.celsius_to_fahrenheit(c)
        print(f"{c}°C is equal to {f}°F")