class TemperatureConverter:
    """A class to convert temperature values between Celsius and Fahrenheit scales."""

    def celsius_to_fahrenheit(self, celsius):
        """
        Converts a given temperature in Celsius to its equivalent in Fahrenheit.

        Args:
            celsius (float or int): The temperature value in degrees Celsius.

        Returns:
            float: The converted temperature in degrees Fahrenheit.
        
        Formula used: F = C * 9/5 + 32
        
        Example:
            >>> converter = TemperatureConverter()
            >>> result = converter.celsius_to_fahrenheit(0)
            >>> return_result == 32.0
            True

        Raises:
            TypeError: If the input `celsius` is not a number (int or float).
        """
        if isinstance(celsius, (int, float)):
            fahrenheit = celsius * 9 / 5 + 32
            return round(fahrenheit)
        else:
            raise TypeError("Input must be an integer or float.")

if __name__ == '__main__':
    # Sample usage without user input, command-line arguments, or network access
    converter = TemperatureConverter()

    sample_celsius_values = [-40, 25.5, 100]

    print("Celsius to Fahrenheit Conversion Results:")
    for c in sample_celsius_values:
        fahrenheit_value = converter.celsius_to_fahrenheit(c)
        print(f"{c}°C is equal to {fahrenheit_value}°F")