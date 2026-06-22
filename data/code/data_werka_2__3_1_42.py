class TemperatureConverter:
    def __init__(self):
        self.conversion_factor = 9 / 5
        self.offset = 32

    def celsius_to_fahrenheit(self, celsius):
        if not isinstance(celsius, (int, float)):
            raise ValueError("Temperature must be a number")
        return (celsius * self.conversion_factor) + self.offset

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
    sample_temperatures_1 = {
        'New York': 10,
        'Los Angeles': 25,
        'Chicago': 15
    }
    converter = TemperatureConverter()
    converted_temperatures_1 = converter.convert_temperatures(sample_temperatures_1)
    print("Converted Temperatures 1:", converted_temperatures_1)

    sample_temperatures_2 = {
        'Tokyo': 15,
        'Beijing': 20,
        'Sydney': 18
    }
    converted_temperatures_2 = converter.convert_temperatures(sample_temperatures_2)
    print("Converted Temperatures 2:", converted_temperatures_2)