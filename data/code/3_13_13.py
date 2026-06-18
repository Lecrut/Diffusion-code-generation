class TemperatureConverter:
    """A class to convert temperatures from Celsius to Fahrenheit."""

    def __init__(self):
        self.celsius_to_fahrenheit_factor = 9 / 5
        self.offset = 32

    def convert_all(self, celsius_readings):
        """
        Converts a list of Celsius temperature readings to Fahrenheit.

        Args:
            celsius_readings (list[float]): A list of temperatures in degrees Celsius.

        Returns:
            list[float]: A new list containing the corresponding temperatures in degrees Fahrenheit.
        """
        fahrenheit_list = []
        for reading in celsius_readings:
            converted_temp = self.celsius_to_fahrenheit_factor * (reading - 0) + self.offset
            fahrenheit_list.append(converted_temp)
        
        return fahrenheit_list

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    celsius_temperatures = [0, 25, -10, 37]

    converter = TemperatureConverter()
    converted_fahrenheit = converter.convert_all(celsius_temperatures)

    print("Celsius -> Fahrenheit Conversion Results:")
    for i in range(len(celsius_temperatures)):
        print(f"{celsius_temperatures[i]}°C is {converted_fahrenheit[i]:.2f}°F")