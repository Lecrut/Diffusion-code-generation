class TemperatureConverter:
    """A class to convert temperatures between Celsius and Fahrenheit."""

    def celsius_to_fahrenheit(self, celsius):
        """
        Converts a temperature from degrees Celsius to degrees Fahrenheit.

        The conversion formula used is: F = (C * 9/5) + 32

        Args:
            celsius (float or int): Temperature in degrees Celsius.

        Returns:
            float: Temperature in degrees Fahrenheit, rounded to two decimal places.
        
        Examples:
            >>> converter = TemperatureConverter()
            >>> converter.celsius_to_fahrenheit(0)
            32.0
            >>> converter.celsius_to_fahrenheit(100)
            212.0
        """
        fahrenheit = (celsius * 9 / 5) + 32
        return round(fahrenheit, 2)

if __name__ == '__main__':
    # Sample usage without user input or external dependencies
    converter = TemperatureConverter()

    sample_celsius_values = [0, 10, 25.5, -40]

    print("Celsius to Fahrenheit Conversion Results:")
    for c in sample_celsius_values:
        fahrenheit_value = converter.celsius_to_fahrenheit(c)
        print(f"{c}°C is equal to {fahrenheit_value}°F")