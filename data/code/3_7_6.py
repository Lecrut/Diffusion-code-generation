class Sensor:
    def __init__(self, raw_value, unit):
        self.raw_value = raw_value
        self.unit = unit

    def get_raw_reading(self):
        return self.raw_value

    def get_unit(self):
        return self.unit

class Converter:
    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == 'celsius' and to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        if from_unit == 'celsius' and to_unit == 'kelvin':
            return value + 273.15
        if from_unit == 'fahrenheit' and to_unit == 'celsius':
            return (value - 32) * 5/9
        if from_unit == 'fahrenheit' and to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
        if from_unit == 'kelvin' and to_unit == 'celsius':
            return value - 273.15
        if from_unit == 'kelvin' and to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32
        raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    sensor = Sensor(25.0, 'celsius')
    converter = Converter()
    raw_temp = sensor.get_raw_reading()
    original_unit = sensor.get_unit()
    fahrenheit_temp = converter.convert(raw_temp, original_unit, 'fahrenheit')
    kelvin_temp = converter.convert(raw_temp, original_unit, 'kelvin')
    print(raw_temp)
    print(fahrenheit_temp)
    print(kelvin_temp)