class TemperatureConverter:
    C_TO_F_FACTOR = 9 / 5
    C_TO_F_OFFSET = 32
    F_TO_C_FACTOR = 5 / 9
    F_TO_C_OFFSET = -32

    @staticmethod
    def celsius_to_fahrenheit(c):
        return c * TemperatureConverter.C_TO_F_FACTOR + TemperatureConverter.C_TO_F_OFFSET

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - TemperatureConverter.F_TO_C_OFFSET) * TemperatureConverter.F_TO_C_FACTOR

if __name__ == '__main__':
    print(TemperatureConverter.celsius_to_fahrenheit(0))
    print(TemperatureConverter.fahrenheit_to_celsius(32))