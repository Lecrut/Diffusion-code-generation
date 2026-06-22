class Sensor:

    def __init__(self):
        self.raw_data = 0

    def read_raw_data(self):
        return self.raw_data

class Converter:
    KELVIN_TO_CELSIUS_OFFSET = 273.15
    FAHRENHEIT_SCALE_FACTOR = 9 / 5

    @staticmethod
    def kelvin_to_celsius(kelvin_temp):
        return kelvin_temp - Converter.KELVIN_TO_CELSIUS_OFFSET

    @staticmethod
    def celsius_to_fahrenheit(celsius_temp):
        return celsius_temp * Converter.FAHRENHEIT_SCALE_FACTOR + 32
if __name__ == '__main__':
    sample_raw_data = 300.0
    sensor = Sensor()
    converter = Converter()
    sensor.raw_data = sample_raw_data
    raw_data = sensor.read_raw_data()
    print(f'Raw Data: {raw_data} K')
    celsius_temperature = converter.kelvin_to_celsius(raw_data)
    print(f'Temperature in Celsius: {celsius_temperature:.2f} °C')
    fahrenheit_temperature = converter.celsius_to_fahrenheit(celsius_temperature)
    print(f'Temperature in Fahrenheit: {fahrenheit_temperature:.2f} °F')