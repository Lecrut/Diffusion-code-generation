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
    raw_temp_celsius = 25.0
    sensor = Sensor(raw_temp_celsius)
    raw_data = sensor.get_raw_temperature()
    converter = Converter()
    temp_fahrenheit = converter.celsius_to_fahrenheit(raw_data)
    print(f'Raw Temperature in Celsius: {raw_data}°C')
    print(f'Converted Temperature in Fahrenheit: {temp_fahrenheit}°F')