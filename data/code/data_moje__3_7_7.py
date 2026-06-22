class Sensor:
    def __init__(self, raw_value):
        self.raw_value = raw_value

    def read(self):
        return self.raw_value

class Converter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9 / 5 + 32

    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit):
        return (fahrenheit - 32) * 5 / 9 + 273.15

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        return (kelvin - 273.15) * 9 / 5 + 32

if __name__ == '__main__':
    sensor = Sensor(100)
    raw_temp = sensor.read()
    celsius_temp = raw_temp
    fahrenheit_temp = Converter.celsius_to_fahrenheit(celsius_temp)
    kelvin_temp = Converter.celsius_to_kelvin(celsius_temp)
    print(fahrenheit_temp)
    print(kelvin_temp)