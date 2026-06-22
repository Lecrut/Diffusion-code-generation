class Sensor:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def read_raw_temperature(self):
        return self.raw_data

class Converter:
    def celsius_to_fahrenheit(self, celsius):
        return celsius * 9 / 5 + 32

    def celsius_to_kelvin(self, celsius):
        return celsius + 273.15

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    def kelvin_to_celsius(self, kelvin):
        return kelvin - 273.15

if __name__ == '__main__':
    sensor = Sensor(25.0)
    raw_temp = sensor.read_raw_temperature()
    converter = Converter()
    fahrenheit = converter.celsius_to_fahrenheit(raw_temp)
    kelvin = converter.celsius_to_kelvin(raw_temp)
    print(fahrenheit)
    print(kelvin)