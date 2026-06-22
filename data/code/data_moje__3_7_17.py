class Sensor:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def read(self):
        return self.raw_data

class Converter:
    @staticmethod
    def to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    @staticmethod
    def to_kelvin(celsius):
        return celsius + 273.15

if __name__ == '__main__':
    sensor = Sensor(98.6)
    raw_temp = sensor.read()
    converter = Converter()
    celsius = converter.to_celsius(raw_temp)
    kelvin = converter.to_kelvin(celsius)
    fahrenheit = converter.to_fahrenheit(celsius)
    print(raw_temp)
    print(celsius)
    print(kelvin)
    print(fahrenheit)