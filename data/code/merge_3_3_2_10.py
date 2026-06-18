class TemperatureConverter:
    """A class to perform temperature conversions between Celsius and Fahrenheit."""
    
    def celsius_to_fahrenheit(self, celsius: float) -> float:
        """
        Converts a temperature value from degrees Celsius to degrees Fahrenheit.

        The conversion formula used is: F = (C * 9/5) + 32

        Args:
            celsius (float): Temperature in degrees Celsius.

        Returns:
            float: Equivalent temperature in degrees Fahrenheit.
        
        Examples:
            >>> converter = TemperatureConverter()
            >>> converter.celsius_to_fahrenheit(0)
            32.0
            >>> converter.celsius_to_fahrenheit(100)
            212.0
        """
        return (celsius * 9 / 5) + 32

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    converter = TemperatureConverter()

    test_cases_celcius = [0, 10, 25, -40]

    for c in test_cases_celcius:
        fahrenheit_value = converter.celsius_to_fahrenheit(c)
        print(f"{c}°C is equal to {fahrenheit_value}°F")