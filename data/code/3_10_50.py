class TemperatureConverter:
    FREEZING_POINT_F = 32
    WATER_BOIL_POINT_F = 212
    ABSOLUTE_ZERO_K = 0

    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit):
        return (fahrenheit - TemperatureConverter.FREEZING_POINT_F) * 5.0 / 9.0 + 273.15

if __name__ == '__main__':
    sample_values = [-40, 0, 32, 100, 212]
    for value in sample_values:
        kelvin_value = TemperatureConverter.fahrenheit_to_kelvin(value)
        print(f"{value}°F is {kelvin_value:.2f}K")