class TemperatureConverter:
    FREEZING_POINT_F = 32
    BOIL_POINT_F = 212
    ABSOLUTE_ZERO_K = 0

    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit):
        return (fahrenheit - TemperatureConverter.FREEZING_POINT_F) * 5 / 9 + 273.15

if __name__ == '__main__':
    sample_values = [TemperatureConverter.FREEZING_POINT_F, TemperatureConverter.BOIL_POINT_F, -40, 100]
    for value in sample_values:
        kelvin_value = TemperatureConverter.fahrenheit_to_kelvin(value)
        print(f"{value} Fahrenheit is {kelvin_value:.2f} Kelvin")