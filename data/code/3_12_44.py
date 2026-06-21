class TemperatureConverter:
    KELVIN_OFFSET = 273.15

    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + TemperatureConverter.KELVIN_OFFSET

if __name__ == '__main__':
    sample_values = {
        'freezing': 0,
        'boiling': 100,
        'absolute_zero': -273.15,
        'human_body': 37
    }
    for name, value in sample_values.items():
        print(f"{name}: {value}C is {TemperatureConverter.celsius_to_kelvin(value)}K")