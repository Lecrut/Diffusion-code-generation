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
    raw_temperature = 25.0
    sensor.read_temperature(raw_temperature)
    fahrenheit_temperature = converter.celsius_to_fahrenheit(sensor.raw_data)
    print(f'Temperature in Fahrenheit: {fahrenheit_temperature}')
    converted_back_celsius = converter.fahrenheit_to_celsius(fahrenheit_temperature)
    print(f'Converted back to Celsius: {converted_back_celsius}')