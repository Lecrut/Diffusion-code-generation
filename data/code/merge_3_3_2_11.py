class TemperatureConverter:
    """
    A utility class to convert temperatures between Celsius and Fahrenheit scales.
    
    Attributes:
        None
    
    Methods:
        celsius_to_fahrenheit(celsius): Converts a temperature value from degrees 
            Celsius (°C) to degrees Fahrenheit (°F).
        
        fahrenheit_to_celsius(fahrenheit): Converts a temperature value from degrees 
            Fahrenheit (°F) to degrees Celsius (°C).

    Examples:
        >>> converter = TemperatureConverter()
        >>> print(converter.celsius_to_fahrenheit(0))
        32.0
        >>> print(converter.fahrenheit_to_celsius(176))
        80.0
    """

    def celsius_to_fahrenheit(self, celsius: float) -> float:
        """
        Converts a temperature from Celsius to Fahrenheit using the formula: 
        F = (C * 9/5) + 32
        
        Args:
            celsius (float): The temperature in degrees Celsius.

        Returns:
            float: The equivalent temperature in degrees Fahrenheit.

        Raises:
            TypeError: If the input is not a numeric type.
        
        >>> converter = TemperatureConverter()
        >>> result = converter.celsius_to_fahrenheit(25)
        >>> assert isinstance(result, float) and abs(result - 77.0) < 1e-6
        """
        if not isinstance(celsius, (int, float)):
            raise TypeError("Input must be a number.")

        return (celsius * 9 / 5) + 32

    def fahrenheit_to_celsius(self, fahrenheit: float) -> float:
        """
        Converts a temperature from Fahrenheit to Celsius using the formula: 
        C = (F - 32) * 5/9
        
        Args:
            fahrenheit (float): The temperature in degrees Fahrenheit.

        Returns:
            float: The equivalent temperature in degrees Celsius.

        Raises:
            TypeError: If the input is not a numeric type.

        >>> converter = TemperatureConverter()
        >>> result = converter.fahrenheit_to_celsius(68)
        >>> assert isinstance(result, float) and abs(result - 20.0) < 1e-6
        """
        if not isinstance(fahrenheit, (int, float)):
            raise TypeError("Input must be a number.")

        return (fahrenheit - 32) * 5 / 9

if __name__ == '__main__':
    converter = TemperatureConverter()
    
    # Sample test cases with hard-coded values
    sample_celsius_values = [0, 25.5, -10]
    sample_fahrenheit_values = [32.0, 86.9, 283.4]

    print("Celsius to Fahrenheit Conversion:")
    for c in sample_celsius_values:
        f_result = converter.celsius_to_fahrenheit(c)
        # Print formatted result (e.g., if input is float, output floats; otherwise integers where possible)
        print(f"{c}°C -> {f_result:.2f}°F")

    print("\nFahrenheit to Celsius Conversion:")
    for f in sample_fahrenheit_values:
        c_result = converter.fahrenheit_to_celsius(f)
        # Format output consistently as float with 1 decimal place or integer if whole number
        formatted_output = f"{c_result:.2f}" 
        print(f"{f}°F -> {formatted_output}°C")

    # Additional verification: round-trip check logic for specific known values
    test_case_fahrenheit = 32.0
    calculated_celsius = converter.fahrenheit_to_celsius(test_case_fahrenheit)
    
    if abs(calculated_celsius - 0.0) < 1e-6:
        print(f"\nVerification Passed: {test_case_fahrenheit}°F correctly converts to 0°C.")
    else:
        print("\nVerification Failed:")