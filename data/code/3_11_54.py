class TemperatureConverter:
    CONVERSION_FACTOR = 9 / 5
    BASE_TEMPERATURE = 32

    @staticmethod
    def celsius_to_fahrenheit(celsius_list):
        return [TemperatureConverter._convert_single(temp) for temp in celsius_list]

    @staticmethod
    def _convert_single(temp):
        if not isinstance(temp, (int, float)):
            raise ValueError("Temperature must be an integer or float.")
        return temp * TemperatureConverter.CONVERSION_FACTOR + TemperatureConverter.BASE_TEMPERATURE

if __name__ == '__main__':
    sample_temperatures = [25, 30, -10, 100]
    try:
        fahrenheit_temperatures = TemperatureConverter.celsius_to_fahrenheit(sample_temperatures)
        print(fahrenheit_temperatures)
    except ValueError as e:
        print(e)