class Sensor:

    def __init__(self, raw_temperature_celsius):
        self.raw_temperature_celsius = raw_temperature_celsius

    def read_raw_temperature(self):
        return self.raw_temperature_celsius

class Converter:

    def celsius_to_fahrenheit(self, celsius):
        return celsius * 9 / 5 + 32

    def celsius_to_kelvin(self, celsius):
        return celsius + 273.15

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    def fahrenheit_to_kelvin(self, fahrenheit):
        celsius = self.fahrenheit_to_celsius(fahrenheit)
        return self.celsius_to_kelvin(celsius)

    def kelvin_to_celsius(self, kelvin):
        return kelvin - 273.15

    def kelvin_to_fahrenheit(self, kelvin):
        celsius = self.kelvin_to_celsius(kelvin)
        return self.celsius_to_fahrenheit(celsius)
if __name__ == '__main__':
    sensor = Sensor(25.5)
    converter = Converter()
    raw_temp = sensor.read_raw_temperature()
    fahrenheit_temp = converter.celsius_to_fahrenheit(raw_temp)
    kelvin_temp = converter.celsius_to_kelvin(raw_temp)
    print(raw_temp)
    print(fahrenheit_temp)
    print(kelvin_temp)
    back_to_celsius = converter.fahrenheit_to_celsius(fahrenheit_temp)
    print(back_to_celsius)
    back_to_celsius_from_kelvin = converter.kelvin_to_celsius(kelvin_temp)
    print(back_to_celsius_from_kelvin)