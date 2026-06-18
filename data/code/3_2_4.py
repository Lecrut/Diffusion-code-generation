class TemperatureConverter:
    """A class to convert temperatures between Celsius and Fahrenheit scales."""

    def celsius_to_fahrenheit(self, celsius):
        """
        Converts a temperature from degrees Celsius to degrees Fahrenheit.

        The formula used is: F = (C * 9/5) + 32

        Args:
            celsius (float or int): Temperature in degrees Celsius.

        Returns:
            float: Converted temperature in degrees Fahrenheit.
        
        Example:
            >>> converter = TemperatureConverter()
            >>> result = converter.celsius_to_fahrenheit(0)
            >>> print(result)  # Output: 32.0
        """
        return (celsius * 9 / 5) + 32

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    converter = TemperatureConverter()

    test_cases = [
        (-40, -40),   # Special case where C equals F
        (0, 32),      # Freezing point of water in Celsius
        (100, 212),   # Boiling point of water in Celsius
        (25.0, 77)    # Room temperature approximation
    ]

    print("Celsius to Fahrenheit Conversion Examples:")
    for c_val, expected_f_val in test_cases:
        result = converter.celsius_to_fahrenheit(c_val)
        status = "PASS" if abs(result - expected_f_val) < 0.1 else f"FAIL (Expected {expected_f_val})"
        print(f"{c_val}°C -> {result}°F [{status}]")