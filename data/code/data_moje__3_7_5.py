class Sensor:
    def __init__(self, raw_reading):
        self.raw_reading = raw_reading

    def read_raw(self):
        return self.raw_reading

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
    sensor = Sensor(100)
    raw = sensor.read_raw()
    
    celsius = raw
    fahrenheit = Converter.celsius_to_fahrenheit(celsius)
    kelvin = Converter.celsius_to_kelvin(celsius)
    
    print(f"Raw: {raw}")
    print(f"Celsius: {celsius}")
    print(f"Fahrenheit: {fahrenheit}")
    print(f"Kelvin: {kelvin}")