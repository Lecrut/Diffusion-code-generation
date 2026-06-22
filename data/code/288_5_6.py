class TemperatureConverter:
    KELVIN_OFFSET = 273.15

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - TemperatureConverter.KELVIN_OFFSET

    @staticmethod
    def temperature_difference(temp_k1, temp_k2):
        celsius_diff = TemperatureConverter.kelvin_to_celsius(temp_k1) - TemperatureConverter.kelvin_to_celsius(temp_k2)
        return abs(celsius_diff)

if __name__ == '__main__':
    result = TemperatureConverter.temperature_difference(300, 295)
    print(result)