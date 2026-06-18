class TemperatureConverter:
    """A utility class to convert temperatures between Celsius and Fahrenheit."""
    
    def celsius_to_fahrenheit(self, celsius: float) -> float:
        """
        Convert a temperature value from degrees Celsius to degrees Fahrenheit.
        
        The conversion formula used is F = (C * 9/5) + 32.0
        
        Args:
            celsius: Temperature in Celsius as a numeric value.
            
        Returns:
            float: The equivalent temperature in Fahrenheit.
            
        Example:
            >>> converter = TemperatureConverter()
            >>> result = converter.celsius_to_fahrenheit(100)
            >>> print(result)  # Output should be approximately 212.0
            
        Note:
            This method uses standard arithmetic operations and does not handle 
            edge cases like infinity or NaN for simplicity, as per the task requirements.
        
        Raises:
            TypeError: If celsius is not a numeric type (int or float).
        """
        if not isinstance(celsius, (int, float)):
            raise TypeError("celsius must be an int or float")
        
        return (celsius * 9 / 5) + 32.0

if __name__ == '__main__':
    # Create an instance of the TemperatureConverter class
    converter = TemperatureConverter()
    
    # Hard-coded sample values for testing without user input
    test_values_celsius = [100, -40, 0]
    
    print("Celsius to Fahrenheit Conversion Results:")
    print("-" * 30)
    
    for val in test_values_celsius:
        fahrenheit_val = converter.celsius_to_fahrenheit(val)
        # Format output with up to two decimal places if it's not a whole number, otherwise as int or float representation
        display_str = (f"{val}°C" + " → ") if isinstance(fahrenheit_val, float) and fahrenheit_val != val else ""
        print(display_str, end="")
        
        # Determine how to display the result based on whether it's a clean integer conversion for clarity
        res_formatted = f"{int(round(fahrenheit_val))}°F" if abs(fahrenheit_val - round(fahrenheit_val)) < 0.1 else str(fahrenheit_val) + "°F"
        
        print(res_formatted)