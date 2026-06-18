class TemperatureConverter:
    def convert_all(self, celsius_readings):
        """
        Convert a list of Celsius temperatures to Fahrenheit.
        
        Args:
            celsius_readings (list[float]): List of temperature values in degrees Celsius.
            
        Returns:
            list[float]: List of corresponding temperature values in degrees Fahrenheit.
        """
        fahrenheit = []
        for c in celsius_readings:
            # Formula: F = C * 9/5 + 32
            temp_f = (c * 18 / 10) + 32
            fahrenheit.append(temp_f)
        return fahrenheit

if __name__ == '__main__':
    converter = TemperatureConverter()

    # Hard-coded sample values
    celsius_list = [0, 25.5, -40, 100]

    result = converter.convert_all(celsius_list)

    print("Celsius to Fahrenheit conversion results:")
    for i in range(len(result)):
        print(f"{celsius_list[i]}°C -> {result[i]:.1f}°F")