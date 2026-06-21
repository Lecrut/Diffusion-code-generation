class TemperatureConverter:
    KELVIN_OFFSET = 273.15
    CELSIUS_TO_FAHRENHEIT_MULTIPLIER = 9/5
    FAHRENHEIT_ADDENDUM = 32

    @staticmethod
    def kelvin_to_celsius(kelvin):
        if kelvin < 0:
            raise ValueError("Kelvin temperature cannot be negative")
        return kelvin - TemperatureConverter.KELVIN_OFFSET

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * TemperatureConverter.CELSIUS_TO_FAHRENHEIT_MULTIPLIER) + TemperatureConverter.FAHRENHEIT_ADDENDUM

    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        celsius = TemperatureConverter.kelvin_to_celsius(kelvin)
        return TemperatureConverter.celsius_to_fahrenheit(celsius)

if __name__ == '__main__':
    sample_kelvin_values = [0, 273.15, 300, 500]
    for kelvin in sample_kelvin_values:
        fahrenheit = TemperatureConverter.kelvin_to_fahrenheit(kelvin)
        print(f"Kelvin: {kelvin} -> Fahrenheit: {fahrenheit}")