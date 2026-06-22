class TemperatureConverter:
    KELVIN_OFFSET = 273.15

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - TemperatureConverter.KELVIN_OFFSET

    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + TemperatureConverter.KELVIN_OFFSET

    @staticmethod
    def temperature_difference(kelvin1, kelvin2):
        return abs(TemperatureConverter.kelvin_to_celsius(kelvin1) - TemperatureConverter.kelvin_to_celsius(kelvin2))

if __name__ == '__main__':
    temp_diff = TemperatureConverter.temperature_difference(300, 298)
    print(temp_diff)