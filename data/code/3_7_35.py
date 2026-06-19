class Sensor:

    def __init__(self, raw_data):
        self.raw_data = raw_data

    def read_raw_temperature(self):
        return self.raw_data

class Converter:

    def celsius_to_fahrenheit(self, celsius):
        return celsius * 9 / 5 + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9
if __name__ == '__main__':
    sample_raw_data = 25.0
    sensor = Sensor(sample_raw_data)
    raw_temperature = sensor.read_raw_temperature()
    print(f'Raw Temperature (Celsius): {raw_temperature}')
    converter = Converter()
    fahrenheit_temperature = converter.celsius_to_fahrenheit(raw_temperature)
    print(f'Temperature in Fahrenheit: {fahrenheit_temperature}')