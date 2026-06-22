class Sensor:

    def __init__(self):
        self.raw_data = 300

    def read_raw_data(self):
        return self.raw_data

class Converter:
    UNIT_CONVERSIONS = {'kelvin_to_celsius': lambda k: k - 273.15, 'celsius_to_fahrenheit': lambda c: c * 9 / 5 + 32}

    def convert(self, raw_data, from_unit, to_unit):
        if f'{from_unit}_to_{to_unit}' in self.UNIT_CONVERSIONS:
            return self.UNIT_CONVERSIONS[f'{from_unit}_to_{to_unit}'](raw_data)
        else:
            raise ValueError(f'Unsupported conversion from {from_unit} to {to_unit}')
if __name__ == '__main__':
    sensor = Sensor()
    converter = Converter()
    raw_data = sensor.read_raw_data()
    print(f'Raw Data in Kelvin: {raw_data}')
    celsius_temperature = converter.convert(raw_data, 'kelvin', 'celsius')
    print(f'Temperature in Celsius: {celsius_temperature:.2f}')
    fahrenheit_temperature = converter.convert(celsius_temperature, 'celsius', 'fahrenheit')
    print(f'Temperature in Fahrenheit: {fahrenheit_temperature:.2f}')