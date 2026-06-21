class TemperatureConverter:
    def __init__(self):
        self.conversion_factor = 9/5
        self.offset = 32

    def celsius_to_fahrenheit(self, celsius):
        return (celsius * self.conversion_factor) + self.offset

    def convert_temperatures(self, temperature_dict):
        return {location: self.celsius_to_fahrenheit(temp) for location, temp in temperature_dict.items()}

if __name__ == '__main__':
    sample_temperatures = {
        'Tokyo': 15,
        'Beijing': 20,
        'Sydney': 18
    }
    converter = TemperatureConverter()
    converted_temperatures = converter.convert_temperatures(sample_temperatures)
    print(converted_temperatures)