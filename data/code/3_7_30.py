class Sensor:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def read_temperature(self):
        return self.raw_data

class Converter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

if __name__ == '__main__':
    raw_temp = Sensor(100)
    celsius_temp = raw_temp.read_temperature()
    print(f"Celsius: {celsius_temp}")
    
    fahrenheit_temp = Converter.celsius_to_fahrenheit(celsius_temp)
    print(f"Fahrenheit: {fahrenheit_temp}")
    
    converted_back_celsius = Converter.fahrenheit_to_celsius(fahrenheit_temp)
    print(f"Converted back to Celsius: {converted_back_celsius}")