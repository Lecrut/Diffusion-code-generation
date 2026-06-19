class Sensor:

    def __init__(self, raw_data):
        self.raw_data = raw_data

    def read_temperature(self):
        return self.raw_data

class Converter:

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9 / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9
if __name__ == '__main__':
    sample_raw_data = 25.0
    sensor = Sensor(sample_raw_data)
    celsius_temperature = sensor.read_temperature()
    fahrenheit_temperature = Converter.celsius_to_fahrenheit(celsius_temperature)
    print(f'Temperature in Fahrenheit: {fahrenheit_temperature}')