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
    raw_temp = 25.0
    sensor = Sensor(raw_temp)
    celsius_temp = sensor.read_temperature()
    converter = Converter()
    fahrenheit_temp = converter.celsius_to_fahrenheit(celsius_temp)
    print(f'Temperature in Celsius: {celsius_temp}°C')
    print(f'Temperature in Fahrenheit: {fahrenheit_temp}°F')