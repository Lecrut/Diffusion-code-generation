class TemperatureConverter:
    CONVERSION_FACTOR = 9 / 5
    OFFSET = 32

    @staticmethod
    def celsius_to_fahrenheit(celsius_list):
        if not all(isinstance(c, (int, float)) for c in celsius_list):
            raise ValueError("All elements in the list must be numbers.")
        return [(c * TemperatureConverter.CONVERSION_FACTOR) + TemperatureConverter.OFFSET for c in celsius_list]

if __name__ == '__main__':
    sample_temperatures = [-50, -10, 0, 25, 100]
    converter = TemperatureConverter()
    fahrenheit_temperatures = converter.celsius_to_fahrenheit(sample_temperatures)
    print(fahrenheit_temperatures)