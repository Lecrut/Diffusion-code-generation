class TemperatureConverter:
    C_TO_F = 9 / 5
    F_TO_C = 5 / 9
    C_OFFSET = 32

    @staticmethod
    def celsius_to_fahrenheit(c):
        return c * TemperatureConverter.C_TO_F + TemperatureConverter.C_OFFSET

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - TemperatureConverter.C_OFFSET) * TemperatureConverter.F_TO_C

if __name__ == '__main__':
    print(TemperatureConverter.celsius_to_fahrenheit(0))
    print(TemperatureConverter.fahrenheit_to_celsius(32))