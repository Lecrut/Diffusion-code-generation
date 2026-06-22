class Sensor:
    def read_celsius(self):
        return 100.0

class Converter:
    def celsius_to_fahrenheit(self, celsius):
        return celsius * 9 / 5 + 32

    def celsius_to_kelvin(self, celsius):
        return celsius + 273.15

if __name__ == '__main__':
    sensor = Sensor()
    converter = Converter()
    raw_temp = sensor.read_celsius()
    fahrenheit = converter.celsius_to_fahrenheit(raw_temp)
    print(fahrenheit)