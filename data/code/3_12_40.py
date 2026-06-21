class TemperatureConverter:
    KELVIN_OFFSET = 273.15

    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + TemperatureConverter.KELVIN_OFFSET

if __name__ == '__main__':
    sample_values = [0, -40, 100, 37]
    for value in sample_values:
        print(f"{value}C is {TemperatureConverter.celsius_to_kelvin(value)}K")