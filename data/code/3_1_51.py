class TemperatureConverter:

    def __init__(self):
        self.factor = 9 / 5
        self.offset = 32

    def convert_celsius_to_fahrenheit(self, celsius):
        if not isinstance(celsius, (int, float)):
            raise ValueError('Temperature must be a number')
        return celsius * self.factor + self.offset

    def process_temperatures(self, temperature_dict):
        if not isinstance(temperature_dict, dict):
            raise ValueError('Input must be a dictionary')
        converted_temps = {}
        for location, temp in temperature_dict.items():
            if not isinstance(location, str):
                raise ValueError('Location keys must be strings')
            if not isinstance(temp, (int, float)):
                raise ValueError('Temperature values must be numbers')
            converted_temp = self.convert_celsius_to_fahrenheit(temp)
            converted_temps[location] = converted_temp
        return converted_temps
if __name__ == '__main__':
    sample_temperatures = {'Paris': 5, 'London': 10, 'Rome': 12}
    converter = TemperatureConverter()
    converted_temperatures = converter.process_temperatures(sample_temperatures)
    print(converted_temperatures)
    single_conversion = converter.convert_celsius_to_fahrenheit(30)
    print(f'Single conversion: 30°C to {single_conversion}°F')