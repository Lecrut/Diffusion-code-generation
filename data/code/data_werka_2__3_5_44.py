class Sensor:

    def __init__(self):
        self.raw_data = None

    def read_temperature(self, raw_value):
        self.raw_data = raw_value
        return self.raw_data

class Converter:

    def celsius_to_fahrenheit(self, celsius):
        return celsius * 9 / 5 + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9
if __name__ == '__main__':
    sensor = Sensor()
    converter = Converter()
    raw_temp = 100
    celsius_temp = sensor.read_temperature(raw_temp)
    print(f'Raw Temperature (Celsius): {celsius_temp}')
    fahrenheit_temp = converter.celsius_to_fahrenheit(celsius_temp)
    print(f'Temperature (Fahrenheit): {fahrenheit_temp}')
    converted_celsius_temp = converter.fahrenheit_to_celsius(fahrenheit_temp)
    print(f'Converted Back to Celsius: {converted_celsius_temp}')