class Sensor:

    def __init__(self, raw_data):
        self.raw_data = raw_data

    def get_raw_data(self):
        return self.raw_data

class Converter:

    def celsius_to_fahrenheit(self, celsius):
        return celsius * 9 / 5 + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9
if __name__ == '__main__':
    sample_raw_data = 25.0
    sensor = Sensor(sample_raw_data)
    converter = Converter()
    raw_celsius = sensor.get_raw_data()
    print(f'Raw Celsius Data: {raw_celsius}')
    fahrenheit = converter.celsius_to_fahrenheit(raw_celsius)
    print(f'Converted to Fahrenheit: {fahrenheit}')
    converted_back_celsius = converter.fahrenheit_to_celsius(fahrenheit)
    print(f'Converted back to Celsius: {converted_back_celsius}')