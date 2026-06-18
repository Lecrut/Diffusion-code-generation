class TemperatureConverter:
    """A utility class to convert temperatures between Celsius and Fahrenheit."""

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """
        Converts a temperature from degrees Celsius to degrees Fahrenheit.

        The conversion formula used is F = (C * 9/5) + 32, where C is the
        temperature in Celsius and F is the temperature in Fahrenheit.

        Args:
            celsius (float): The temperature in degrees Celsius.

        Returns:
            float: The equivalent temperature in degrees Fahrenheit.
        """
        return (celsius * 9 / 5) + 32

if __name__ == '__main__':
    # Sample conversions without user input or external dependencies
    converter = TemperatureConverter()

    sample_celcius_values = [0, 18, -40, 100]

    print("Celsius to Fahrenheit Conversion Results:")
    for c in sample_celcius_values:
        fahrenheit_value = converter.celsius_to_fahrenheit(c)
        print(f"{c}°C is equal to {fahrenheit_value:.2f}°F")