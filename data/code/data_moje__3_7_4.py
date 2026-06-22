class Sensor:
    def __init__(self, raw_value):
        self.raw_value = raw_value

    def read_temperature(self):
        return self.raw_value

class Converter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9 / 5 + 32

    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15

if __name__ == '__main__':
    sensor = Sensor(25.0)
    raw_temp = sensor.read_temperature()
    converter = Converter()
    fahrenheit = converter.celsius_to_fahrenheit(raw_temp)
    kelvin = converter.celsius_to_kelvin(raw_temp)
    print(fahrenheit)
    print(kelvin)