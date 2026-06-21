class Sensor:

    def __init__(self, raw_data):
        self.raw_data = raw_data

    def read_raw_data(self):
        return self.raw_data

class Converter:

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9 / 5 + 32
if __name__ == '__main__':
    sample_raw_data = 365
    sensor = Sensor(sample_raw_data)
    raw_data = sensor.read_raw_data()
    print(f'Raw Data: {raw_data} K')
    celsius = Converter.kelvin_to_celsius(raw_data)
    print(f'Temperature in Celsius: {celsius:.2f} °C')
    fahrenheit = Converter.celsius_to_fahrenheit(celsius)
    print(f'Temperature in Fahrenheit: {fahrenheit:.2f} °F')