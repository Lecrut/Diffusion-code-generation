class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9 / 5 + 32

    def convert_all(self, celsius_readings):
        return [self.celsius_to_fahrenheit(c) for c in celsius_readings]

if __name__ == '__main__':
    converter = TemperatureConverter()
    celsius_values = [0, 100, 37, -40, 212]
    fahrenheit_values = converter.convert_all(celsius_values)
    print(fahrenheit_values)