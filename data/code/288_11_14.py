class TemperatureConverter:
    KELVIN_TO_CELSIUS = -273.15

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin + TemperatureConverter.KELVIN_TO_CELSIUS

    @staticmethod
    def difference_in_celsius(temp1, temp2):
        celsius1 = TemperatureConverter.kelvin_to_celsius(temp1)
        celsius2 = TemperatureConverter.kelvin_to_celsius(temp2)
        return abs(celsius1 - celsius2)
if __name__ == '__main__':
    result = TemperatureConverter.difference_in_celsius(300, 280)
    print(result)