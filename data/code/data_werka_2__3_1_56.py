class TemperatureConverter:
    CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
    FAHRENHEIT_OFFSET = 32

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * TemperatureConverter.CELSIUS_TO_FAHRENHEIT_FACTOR) + TemperatureConverter.FAHRENHEIT_OFFSET

    def convert_temperatures(self, temperature_dict):
        if not isinstance(temperature_dict, dict):
            raise ValueError("Input must be a dictionary")
        converted_dict = {}
        for location, temp in temperature_dict.items():
            if not isinstance(location, str):
                raise ValueError("Location keys must be strings")
            if not isinstance(temp, (int, float)):
                raise ValueError("Temperature values must be numbers")
            converted_temp = self.celsius_to_fahrenheit(temp)
            converted_dict[location] = converted_temp
        return converted_dict

if __name__ == '__main__':
    sample_temperatures = {
        'Paris': 12,
        'London': 8,
        'Rome': 14
    }
    converter = TemperatureConverter()
    converted_temperatures = converter.convert_temperatures(sample_temperatures)
    print(converted_temperatures)