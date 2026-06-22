class Sensor:

    def __init__(self, raw_data):
        self.raw_data = raw_data

    def get_raw_temperature(self):
        return self.raw_data

class Converter:

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9 / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9
if __name__ == '__main__':
    raw_temperature = 25.0
    sensor = Sensor(raw_temperature)
    converter = Converter()
    celsius_temp = sensor.get_raw_temperature()
    fahrenheit_temp = converter.celsius_to_fahrenheit(celsius_temp)
    print(f'Celsius: {celsius_temp}, Fahrenheit: {fahrenheit_temp}')