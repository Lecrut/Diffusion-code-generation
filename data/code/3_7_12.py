class Sensor:
    def __init__(self, celsius):
        self.celsius = celsius

    def read(self):
        return self.celsius

class Converter:
    def to_fahrenheit(self, celsius):
        return (celsius * 9 / 5) + 32

    def to_kelvin(self, celsius):
        return celsius + 273.15

if __name__ == '__main__':
    raw_temp = 25.0
    sensor = Sensor(raw_temp)
    converter = Converter()
    celsius_val = sensor.read()
    fahrenheit_val = converter.to_fahrenheit(celsius_val)
    kelvin_val = converter.to_kelvin(celsius_val)
    print(fahrenheit_val)
    print(kelvin_val)