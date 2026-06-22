class Sensor:
    def __init__(self, raw_temperature):
        self.raw_temperature = raw_temperature

    def read_raw(self):
        return self.raw_temperature

class Converter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit):
        return (fahrenheit - 32) * 5/9 + 273.15

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        return (kelvin - 273.15) * 9/5 + 32

if __name__ == '__main__':
    sensor = Sensor(25.0)
    raw_temp = sensor.read_raw()
    
    converter = Converter()
    
    fahrenheit = converter.celsius_to_fahrenheit(raw_temp)
    kelvin = converter.celsius_to_kelvin(raw_temp)
    
    print(raw_temp)
    print(fahrenheit)
    print(kelvin)