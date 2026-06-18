class TemperatureConverter:
    """A class to convert temperatures between Celsius and Fahrenheit."""

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """Converts a temperature value from Celsius to Fahrenheit.

        The conversion formula used is F = (C * 9/5) + 32.

        Args:
            celsius (float): The temperature in degrees Celsius.

        Returns:
            float: The equivalent temperature in degrees Fahrenheit.

        Examples:
            >>> converter = TemperatureConverter()
            >>> result = converter.celsius_to_fahrenheit(0)
            >>> print(result == 32.0)
            True
            >>> result = converter.celsius_to_fahrenheit(100)
            >>> print(round(result, 2))
            212.0
        """
        return (celsius * 9 / 5) + 32

if __name__ == '__main__':
    # Sample test cases with hard-coded values to ensure the module runs without user input or files.
    converter = TemperatureConverter()

    celsius_values = [0, 10, -40, 100]

    print("Temperature Conversion Results (Celsius -> Fahrenheit):")
    for c in celsius_values:
        fahrenheit = converter.celsius_to_fahrenheit(c)
        # Using round to ensure clean output for integer-like inputs like -40 and 100 which are exact matches.
        formatted_result = str(round(fahrenheit, 2)) if float(formatted_result).is_integer() else formatted_result
        print(f"{c}°C is equal to {formatted_result}°F")