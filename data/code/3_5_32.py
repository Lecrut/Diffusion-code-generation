class Sensor:
    def __init__(self):
        self.raw_data = 365
    
    def read_raw_data(self):
        return self.raw_data

class Converter:
    def __init__(self):
        self.name = "TemperatureConverter"
    
    def convert_to_celsius(self, raw_data):
        return raw_data - 273.15
    
    def convert_to_fahrenheit(self, celsius):
        return celsius * 9 / 5 + 32

if __name__ == '__main__':
    sensor = Sensor()
    converter = Converter()
    
    raw_data = sensor.read_raw_data()
    print(f'Raw Data: {raw_data}')
    
    celsius = converter.convert_to_celsius(raw_data)
    print(f'Celsius: {celsius:.2f}')
    
    fahrenheit = converter.convert_to_fahrenheit(celsius)
    print(f'Fahrenheit: {fahrenheit:.2f}')