class TemperatureConverter:
    """A class to convert temperatures from Celsius to Fahrenheit."""

    def __init__(self):
        pass

    def convert_all(self, celsius_readings):
        """
        Converts a list of Celsius temperature readings to their Fahrenheit equivalents.

        Args:
            celsius_readings (list[float]): A list containing numeric values in degrees Celsius.

        Returns:
            list[float]: A new list with corresponding temperatures converted to Fahrenheit.
        
        Formula used: F = C * 9/5 + 32
        """
        fahrenheit_list = []
        for celsius_value in celsius_readings:
            # Apply the conversion formula directly within the loop for efficiency and clarity
            fahrenheit_value = (celsius_value * 1.8) + 32
            fahrenheit_list.append(fahrenheit_value)
        
        return fahrenheit_list

if __name__ == '__main__':
    # Hard-coded sample values as per requirements; no user input or external dependencies needed
    celsius_temperatures = [0, 15.6, -40, 37]

    converter = TemperatureConverter()
    converted_fahrenheit = converter.convert_all(celsius_temperatures)

    print("Celsius to Fahrenheit Conversion Results:")
    for i in range(len(converted_fahrenheit)):
        print(f"{celsius_temperatures[i]}°C -> {converted_fahrenheit[i]:.2f}°F")