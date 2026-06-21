class Sensor:
    def __init__(self):
        self.raw_data = 300

    def read_raw_data(self):
        return self.raw_data

class Converter:
    KELVIN_OFFSET = 273.15

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - Converter.KELVIN_OFFSET

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

if __name__ == '__main__':
    sensor = Sensor()
    converter = Converter()

    raw_data = sensor.read_raw_data()
    print(f'Raw Data: {raw_data}K')

    celsius_temperature = converter.kelvin_to_celsius(raw_data)
    print(f'Temperature in Celsius: {celsius_temperature:.2f}°C')

    fahrenheit_temperature = converter.celsius_to_fahrenheit(celsius_temperature)
    print(f'Temperature in Fahrenheit: {fahrenheit_temperature:.2f}°F')