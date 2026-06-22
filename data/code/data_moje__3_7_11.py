class Sensor:
    def __init__(self, reading_fahrenheit):
        self.reading_fahrenheit = float(reading_fahrenheit)

    def get_raw_reading(self):
        return self.reading_fahrenheit

class Converter:
    @staticmethod
    def celsius_from_fahrenheit(fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def kelvin_from_fahrenheit(fahrenheit):
        return (fahrenheit - 32) * 5 / 9 + 273.15

if __name__ == '__main__':
    sensor = Sensor(212.0)
    raw_temp = sensor.get_raw_reading()
    converter = Converter()
    celsius = converter.celsius_from_fahrenheit(raw_temp)
    kelvin = converter.kelvin_from_fahrenheit(raw_temp)
    print(celsius)
    print(kelvin)