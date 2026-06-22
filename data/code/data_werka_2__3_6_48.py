class TemperatureConverter:
    CONVERSION_FACTOR = 9 / 5
    BASE_OFFSET = 32

    @staticmethod
    def convert_temp(celsius_list):
        return [c * TemperatureConverter.CONVERSION_FACTOR + TemperatureConverter.BASE_OFFSET for c in celsius_list]

if __name__ == '__main__':
    sample_temps = [-40, 0, 100, 37]
    fahrenheit_temps = TemperatureConverter.convert_temp(sample_temps)
    print(fahrenheit_temps)