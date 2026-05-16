class Sensor:
    def read_raw_temperature(self):
        return 25.5
class Converter:
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32
class TemperatureSystem:
    def __init__(self):
        self.sensor = Sensor()
        self.converter = Converter()
    def get_temperature_in_fahrenheit(self):
        raw_temp = self.sensor.read_raw_temperature()
        fahrenheit = self.converter.celsius_to_fahrenheit(raw_temp)
        return fahrenheit
if __name__ == '__main__':
    system = TemperatureSystem()
    fahrenheit_temp = system.get_temperature_in_fahrenheit()
    print(fahrenheit_temp)