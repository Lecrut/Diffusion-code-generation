class Sensor:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def read_raw_temperature(self):
        return self.raw_data

class Converter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit):
        celsius = Converter.fahrenheit_to_celsius(fahrenheit)
        return Converter.celsius_to_kelvin(celsius)

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        celsius = Converter.kelvin_to_celsius(kelvin)
        return Converter.celsius_to_fahrenheit(celsius)

if __name__ == '__main__':
    sensor = Sensor(25.0)
    raw_temp = sensor.read_raw_temperature()
    print(raw_temp)
    converter = Converter()
    fahrenheit = converter.celsius_to_fahrenheit(raw_temp)
    print(fahrenheit)
    kelvin = converter.celsius_to_kelvin(raw_temp)
    print(kelvin)
    back_to_celsius = converter.fahrenheit_to_celsius(fahrenheit)
    print(back_to_celsius)