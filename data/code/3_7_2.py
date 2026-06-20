class Sensor:
    def __init__(self):
        self.raw_data = None

    def read_raw_temperature(self, value):
        self.raw_data = value
        return self.raw_data

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
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

if __name__ == '__main__':
    sensor = Sensor()
    converter = Converter()

    raw_celsius = sensor.read_raw_temperature(25.0)
    print(raw_celsius)

    fahrenheit = converter.celsius_to_fahrenheit(raw_celsius)
    print(fahrenheit)

    kelvin = converter.celsius_to_kelvin(raw_celsius)
    print(kelvin)

    back_to_celsius = converter.fahrenheit_to_celsius(fahrenheit)
    print(back_to_celsius)

    back_to_celsius_k = converter.kelvin_to_celsius(kelvin)
    print(back_to_celsius_k)