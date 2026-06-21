class TemperatureConverter:
    FAHRENHEIT_FACTOR = 9 / 5
    FAHRENHEIT_OFFSET = 32

    @staticmethod
    def convert(celsius):
        return (celsius * TemperatureConverter.FAHRENHEIT_FACTOR) + TemperatureConverter.FAHRENHEIT_OFFSET

    def convert_all(self, celsius_readings):
        if not all(isinstance(c, (int, float)) for c in celsius_readings):
            raise ValueError("All elements must be numbers representing Celsius temperatures.")
        return [TemperatureConverter.convert(c) for c in celsius_readings]

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_celsius = [15, -30, 22.5, 100]
    fahrenheit_readings = converter.convert_all(sample_celsius)
    print(fahrenheit_readings)