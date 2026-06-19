class Sensor:

    def __init__(self, raw_data):
        self.raw_data = raw_data

    def read_raw_temperature(self):
        return self.raw_data

class Converter:

    def __init__(self, temperature_in_celsius):
        self.temperature_in_celsius = temperature_in_celsius

    def to_fahrenheit(self):
        return self.temperature_in_celsius * 9 / 5 + 32

    def to_kelvin(self):
        return self.temperature_in_celsius + 273.15
if __name__ == '__main__':
    sample_raw_data = 25.0
    sensor = Sensor(sample_raw_data)
    raw_temperature = sensor.read_raw_temperature()
    converter = Converter(raw_temperature)
    fahrenheit = converter.to_fahrenheit()
    kelvin = converter.to_kelvin()
    print(f'Temperature in Fahrenheit: {fahrenheit}')
    print(f'Temperature in Kelvin: {kelvin}')