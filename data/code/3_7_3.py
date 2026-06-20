class Sensor:
    def __init__(self, raw_value):
        self.raw_value = raw_value

    def get_raw_data(self):
        return self.raw_value

class Converter:
    def celsius_to_fahrenheit(self, celsius):
        return celsius * 9 / 5 + 32

    def celsius_to_kelvin(self, celsius):
        return celsius + 273.15

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9

if __name__ == '__main__':
    sensor = Sensor(25.0)
    raw_data = sensor.get_raw_data()
    
    converter = Converter()
    fahrenheit = converter.celsius_to_fahrenheit(raw_data)
    kelvin = converter.celsius_to_kelvin(raw_data)
    
    print(fahrenheit)
    print(kelvin)