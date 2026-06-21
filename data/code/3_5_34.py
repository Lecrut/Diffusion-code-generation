class Sensor:

    def __init__(self):
        self.raw_data = None

    def read_temperature(self, raw_value):
        self.raw_data = raw_value

class Converter:

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9 / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9
if __name__ == '__main__':
    sensor = Sensor()
    converter = Converter()
    raw_temperature_celsius = 25.0
    sensor.read_temperature(raw_temperature_celsius)
    converted_temperature_fahrenheit = converter.celsius_to_fahrenheit(sensor.raw_data)
    print(f'Temperature in Fahrenheit: {converted_temperature_fahrenheit}')
    converted_back_temperature_celsius = converter.fahrenheit_to_celsius(converted_temperature_fahrenheit)
    print(f'Converted back to Celsius: {converted_back_temperature_celsius}')