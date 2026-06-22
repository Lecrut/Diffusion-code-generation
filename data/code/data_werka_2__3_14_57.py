class TemperatureConverter:
    KELVIN_OFFSET = 273.15
    FAHRENHEIT_SCALE_FACTOR = 9/5

    @staticmethod
    def kelvin_to_celsius(kelvin):
        if kelvin < 0:
            raise ValueError("Kelvin temperature cannot be negative")
        return kelvin - TemperatureConverter.KELVIN_OFFSET

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * TemperatureConverter.FAHRENHEIT_SCALE_FACTOR) + 32

    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        celsius = TemperatureConverter.kelvin_to_celsius(kelvin)
        return TemperatureConverter.celsius_to_fahrenheit(celsius)

if __name__ == '__main__':
    sample_kelvin_values = [0, 273.15, 300, 500]
    for kelvin in sample_kelvin_values:
        fahrenheit = TemperatureConverter.kelvin_to_fahrenheit(kelvin)
        print(f"Kelvin: {kelvin} -> Fahrenheit: {fahrenheit}")