class Sensor:

    def __init__(self, raw_data):
        self.raw_data = raw_data

    def read_raw_temperature(self):
        return self.raw_data

class Converter:

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9 / 5 + 32
if __name__ == '__main__':
    sample_raw_data = 300.0
    sensor = Sensor(sample_raw_data)
    raw_temperature_kelvin = sensor.read_raw_temperature()
    print(f'Raw Temperature in Kelvin: {raw_temperature_kelvin}')
    converter = Converter()
    celsius_temperature = converter.kelvin_to_celsius(raw_temperature_kelvin)
    print(f'Temperature in Celsius: {celsius_temperature:.2f}')
    fahrenheit_temperature = converter.celsius_to_fahrenheit(celsius_temperature)
    print(f'Temperature in Fahrenheit: {fahrenheit_temperature:.2f}')