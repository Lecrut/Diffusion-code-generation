class TemperatureConverter:
    """A class to convert temperatures from Celsius to Fahrenheit."""

    def __init__(self):
        """Initialize the TemperatureConverter instance with no specific parameters needed."""
        pass

    def convert_all(self, celsius_readings):
        """
        Convert a list of Celsius temperature readings to their corresponding Fahrenheit values.

        The conversion formula used is: F = (C * 9/5) + 32

        Args:
            celsius_readings (list[float]): A list containing numeric values representing temperatures in degrees Celsius.

        Returns:
            list[float]: A new list containing the converted Fahrenheit temperature values corresponding to each input reading.
        
        Raises:
            TypeError: If the input is not a list or contains non-numeric elements that cannot be cast to float.
        """
        if not isinstance(celsius_readings, list):
            raise TypeError("Input must be a list.")

        fahrenheit_results = []
        for c in celsius_readings:
            try:
                c_float = float(c)
                f_result = (c_float * 9 / 5) + 32
                fahrenheit_results.append(f_result)
            except ValueError as e:
                raise TypeError("All elements in the list must be numeric.") from e

        return fahrenheit_results

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    celsius_temps = [0, 25, -10, 37]
    
    converter = TemperatureConverter()
    converted_fahreneight = converter.convert_all(celsius_temps)

    print("Celsius to Fahrenheit Conversion Results:")
    for i in range(len(converted_fahreneight)):
        print(f"{celsius_temps[i]}°C -> {converted_fahreneight[i]:.2f}°F")