class Sensor:

    def __init__(self, raw_data):
        self.raw_data = raw_data

    def get_raw_temperature(self):
        return self.raw_data

class Converter:

    def celsius_to_fahrenheit(self, celsius):
        return celsius * 9 / 5 + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9
if __name__ == '__main__':
    sample_raw_data = 25.0
    sensor = Sensor(sample_raw_data)
    raw_temperature_celsius = sensor.get_raw_temperature()
    converter = Converter()
    converted_temperature_fahrenheit = converter.celsius_to_fahrenheit(raw_temperature_celsius)
    print(f'Converted Temperature: {converted_temperature_fahrenheit}°F')