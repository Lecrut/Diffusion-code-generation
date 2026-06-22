class Sensor:

    def __init__(self, raw_data):
        self.raw_data = raw_data

    def read_temperature(self):
        return self.raw_data

class Converter:

    def celsius_to_fahrenheit(self, celsius):
        return celsius * 9 / 5 + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9
if __name__ == '__main__':
    sample_raw_data = 25.0
    sensor = Sensor(sample_raw_data)
    celsius_temperature = sensor.read_temperature()
    converter = Converter()
    fahrenheit_temperature = converter.celsius_to_fahrenheit(celsius_temperature)
    print(f'Original Temperature (Celsius): {celsius_temperature}')
    print(f'Converted Temperature (Fahrenheit): {fahrenheit_temperature}')