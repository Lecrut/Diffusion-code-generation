class TemperatureConverter:
    C_TO_F_FACTOR = 9 / 5
    C_TO_F_OFFSET = 32
    F_TO_C_FACTOR = 5 / 9
    F_TO_C_OFFSET = 32
    K_TO_C_OFFSET = 273.15

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * TemperatureConverter.C_TO_F_FACTOR + TemperatureConverter.C_TO_F_OFFSET

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - TemperatureConverter.F_TO_C_OFFSET) * TemperatureConverter.F_TO_C_FACTOR

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - TemperatureConverter.K_TO_C_OFFSET

if __name__ == '__main__':
    converter = TemperatureConverter()
    print(converter.celsius_to_fahrenheit(25))
    print(converter.fahrenheit_to_celsius(98.6))
    print(converter.kelvin_to_celsius(300))