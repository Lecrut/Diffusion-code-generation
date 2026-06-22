class TemperatureConverter:
    def __init__(self, kelvin):
        self.kelvin = kelvin

    def to_celsius(self):
        return self.kelvin - 273.15

    def to_fahrenheit(self):
        return (self.kelvin - 273.15) * 9/5 + 32

    def to_rankine(self):
        return self.kelvin * 9/5

if __name__ == '__main__':
    converter = TemperatureConverter(20)
    print(converter.to_celsius())
    print(converter.to_fahrenheit())
    print(converter.to_rankine())