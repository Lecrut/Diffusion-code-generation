class TemperatureConverter:
    """A class to convert temperature values between Celsius and Fahrenheit."""

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """
        Convert a temperature value from degrees Celsius to degrees Fahrenheit.

        The conversion formula used is F = (C * 9/5) + 32, where C is the
        temperature in Celsius and F is the result in Fahrenheit.

        Args:
            celsius (float): Temperature value in Celsius.

        Returns:
            float: Converted temperature value in Fahrenheit.

        Example:
            >>> converter = TemperatureConverter()
            >>> converter.celsius_to_fahrenheit(0)
            32.0
            >>> converter.celsius_to_fahrenheit(100)
            212.0
        """
        return (celsius * 9 / 5) + 32

if __name__ == '__main__':
    # Sample conversions without user input or external dependencies
    sample_celsius_values = [0, 25, -40, 100]

    converter = TemperatureConverter()

    for c in sample_celsius_values:
        fahrenheit_value = converter.celsius_to_fahrenheit(c)
        print(f"{c}°C is equal to {fahrenheit_value}°F")