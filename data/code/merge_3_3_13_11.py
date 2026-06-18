class TemperatureConverter:
    """A class to convert temperatures from Celsius to Fahrenheit."""

    def __init__(self):
        pass

    def convert_all(self, celsius_readings):
        """
        Converts a list of Celsius temperature readings to their equivalent in Fahrenheit.

        Args:
            celsius_readings (list[float]): A list containing numeric values representing temperatures in degrees Celsius.

        Returns:
            list[float]: A new list with the corresponding temperatures converted to degrees Fahrenheit.
        
        Formula used: F = C * 9/5 + 32
        """
        fahrenheit_list = []
        for celsius_temp in celsius_readings:
            # Apply conversion formula directly within loop or use map/list comprehension
            fahrenheit_temp = (celsius_temp * 1.8) + 32
            fahrenheit_list.append(fahrenheit_temp)
        
        return fahrenheit_list

if __name__ == '__main__':
    # Hard-coded sample values as per requirements, no user input or external dependencies needed
    celsius_temps = [0, 25.5, -10, 37]

    converter = TemperatureConverter()
    converted_temps = converter.convert_all(celsius_temps)

    print("Celsius to Fahrenheit Conversion Results:")
    for i in range(len(converted_temps)):
        print(f"{celsius_temps[i]}°C -> {converted_temps[i]:.2f}°F")