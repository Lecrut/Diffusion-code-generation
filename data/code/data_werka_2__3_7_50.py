class TemperatureConverter:
    CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
    FAHRENHEIT_OFFSET = 32

    @staticmethod
    def convert(celsius):
        return (celsius * TemperatureConverter.CELSIUS_TO_FAHRENHEIT_FACTOR) + TemperatureConverter.FAHRENHEIT_OFFSET

    def convert_all(self, celsius_readings):
        if not isinstance(celsius_readings, list):
            raise ValueError("Input must be a list of Celsius temperatures.")
        return [TemperatureConverter.convert(c) for c in celsius_readings]

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_celsius = [-20, -10, 0, 15, 30]
    fahrenheit_readings = converter.convert_all(sample_celsius)
    print(fahrenheit_readings)