class TemperatureConverter:
    """A class to convert temperatures between Celsius and Fahrenheit."""

    def celsius_to_fahrenheit(self, celsius):
        """Converts a temperature from degrees Celsius to degrees Fahrenheit.

        Args:
            celsius (float or int): The temperature in degrees Celsius.

        Returns:
            float: The equivalent temperature in degrees Fahrenheit.

        Formula used: F = C * 9/5 + 32
        """
        return celsius * 1.8 + 32

if __name__ == '__main__':
    # Sample values for testing the conversion logic without user input or external dependencies
    test_cases = [0, 25, -40, 100]

    converter = TemperatureConverter()

    print("Celsius to Fahrenheit Conversion Results:")
    for c in test_cases:
        fahrenheit_value = converter.celsius_to_fahrenheit(c)
        print(f"{c}°C is equal to {fahrenheit_value:.2f}°F")