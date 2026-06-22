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

    def __init__(self, kelvin):
        self.kelvin = kelvin

    def convert_to_fahrenheit(self):
        celsius = TemperatureConverter.kelvin_to_celsius(self.kelvin)
        return TemperatureConverter.celsius_to_fahrenheit(celsius)

if __name__ == '__main__':
    sample_kelvin_values = [0, 273.15, 300, 500]
    for kelvin in sample_kelvin_values:
        converter = TemperatureConverter(kelvin)
        fahrenheit = converter.convert_to_fahrenheit()
        print(f"Kelvin: {kelvin} -> Fahrenheit: {fahrenheit}")