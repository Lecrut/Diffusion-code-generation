class Sensor:
    def __init__(self):
        self.raw_data = None

    def read_temperature(self, raw_value):
        self.raw_data = raw_value
        return self.raw_data

class Converter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

if __name__ == '__main__':
    sensor = Sensor()
    raw_temp = sensor.read_temperature(25)
    print("Raw Temperature:", raw_temp)

    converter = Converter()
    fahrenheit_temp = converter.celsius_to_fahrenheit(raw_temp)
    print("Temperature in Fahrenheit:", fahrenheit_temp)

    celsius_temp = converter.fahrenheit_to_celsius(fahrenheit_temp)
    print("Converted back to Celsius:", celsius_temp)