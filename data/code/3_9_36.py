class TemperatureConverter:
    FAHRENHEIT_OFFSET = 32
    CONVERSION_RATIO = 9/5

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * TemperatureConverter.CONVERSION_RATIO) + TemperatureConverter.FAHRENHEIT_OFFSET

def convert_temp(celsius_list):
    converter = TemperatureConverter()
    return [converter.celsius_to_fahrenheit(c) for c in celsius_list]

if __name__ == '__main__':
    sample_temperatures_celsius = [-40, 0, 25, 100]
    converted_temperatures_fahrenheit = convert_temp(sample_temperatures_celsius)
    print(converted_temperatures_fahrenheit)