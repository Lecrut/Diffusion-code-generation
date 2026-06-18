class TemperatureConverter:
    """A class to convert temperatures between Celsius and Fahrenheit."""

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """
        Converts a temperature from degrees Celsius to degrees Fahrenheit.

        The conversion formula used is: F = (C * 9/5) + 32.0

        Args:
            celsius (float): Temperature in degrees Celsius.

        Returns:
            float: Temperature in degrees Fahrenheit.
        
        Examples:
            >>> converter.celsius_to_fahrenheit(0)
            32.0
            >>> converter.celsius_to_fahrenheit(100)
            212.0
        """
        return (celsius * 9 / 5) + 32.0

if __name__ == '__main__':
    # Sample values to test the conversion functionality without user input
    
    # Test case 1: Freezing point of water in Celsius -> Fahrenheit
    c_temp_1 = 0.0
    f_result_1 = TemperatureConverter.celsius_to_fahrenheit(c_temp_1)

    # Test case 2: Boiling point of water in Celsius -> Fahrenheit
    c_temp_2 = 100.0
    f_result_2 = TemperatureConverter.celsius_to_fahrenheit(c_temp_2)

    # Display results
    print(f"{c_temp_1}°C is equal to {f_result_1:.2f}°F")
    print(f"{c_temp_2}°C is equal to {f_result_2:.2f}°F")