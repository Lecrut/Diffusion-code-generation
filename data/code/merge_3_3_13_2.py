class TemperatureConverter:
    def convert_all(self, celsius_readings):
        """Converts a list of Celsius temperatures to Fahrenheit."""
        fahrenheit_temperatures = []
        for degree_c in celsius_readings:
            if not isinstance(degree_c, (int, float)):
                raise TypeError("All elements must be numeric.")
            f_degree = (degree_c * 9) / 5 + 32
            fahrenheit_temperatures.append(f_degree)
        return fahrenheit_temperatures

if __name__ == '__main__':
    converter_instance = TemperatureConverter()

    sample_celsius_data = [0, 18, 36.11]

    converted_fahrenheit_data = converter_instance.convert_all(sample_celsius_data)

    print("Celsius to Fahrenheit Conversion Results:")
    for i in range(len(converted_fahrenheit_data)):
        print(f"{sample_celsius_data[i]}°C is {converted_fahrenheit_data[i]:.2f}°F")