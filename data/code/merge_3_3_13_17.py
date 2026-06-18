class TemperatureConverter:
    """A class to convert temperatures from Celsius to Fahrenheit."""

    def __init__(self):
        self.celsius_to_fahrenheit = 9 / 5
        self.offset = 32

    def convert_all(self, celsius_readings):
        """
        Converts a list of Celsius temperature readings to Fahrenheit.

        Args:
            celsius_readings (list[float]): A list containing numerical values in degrees Celsius.

        Returns:
            list[float]: A new list with corresponding temperatures converted to degrees Fahrenheit.
        """
        fahrenheit_list = []
        for reading in celsius_readings:
            # Formula: F = C * 9/5 + 32
            fahrenheit_value = (reading * self.celsius_to_fahrenheit) + self.offset
            fahrenheit_list.append(fahrenheit_value)

        return fahrenheit_list

if __name__ == '__main__':
    sample_celsius_temps = [0, 10.5, -4, 25]
    
    converter = TemperatureConverter()
    converted_temps = converter.convert_all(sample_celsius_temps)
    
    print("Celsius to Fahrenheit Conversion:")
    for i in range(len(converted_temps)):
        print(f"{sample_celsius_temps[i]}°C -> {converted_temps[i]:.2f}°F")