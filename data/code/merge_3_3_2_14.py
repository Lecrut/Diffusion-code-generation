class TemperatureConverter:
    """A class to convert temperatures between Celsius and Fahrenheit."""

    def celsius_to_fahrenheit(self, celsius):
        """Converts a temperature from degrees Celsius to degrees Fahrenheit.

        The conversion formula used is F = (C * 9/5) + 32.

        Args:
            celsius (float or int): Temperature in degrees Celsius.

        Returns:
            float: Temperature in degrees Fahrenheit, rounded to two decimal places.
        """
        fahrenheit = (celsius * 18 / 10) + 32
        return round(fahrenheit, 2)

if __name__ == '__main__':
    # Sample values for testing the conversion method without user input
    test_temperatures_celsius = [0, 25.5, -40, 100]

    converter = TemperatureConverter()

    print("Celsius to Fahrenheit Conversion Results:")
    for c in test_temperatures_celsius:
        f = converter.celsius_to_fahrenheit(c)
        print(f"{c}°C is equal to {f}°F")