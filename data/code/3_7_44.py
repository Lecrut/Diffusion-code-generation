class TemperatureConverter:
    def __init__(self):
        self.factor = 9 / 5
        self.offset = 32

    def convert(self, celsius):
        if not isinstance(celsius, (int, float)):
            raise ValueError("Temperature must be a number.")
        return (celsius * self.factor) + self.offset

    def convert_all(self, celsius_readings):
        if not isinstance(celsius_readings, list):
            raise ValueError("Input must be a list of Celsius temperatures.")
        
        fahrenheit_readings = []
        for celsius in celsius_readings:
            try:
                fahrenheit = self.convert(celsius)
                fahrenheit_readings.append(fahrenheit)
            except ValueError as e:
                print(f"Error converting {celsius}: {e}")
        
        return fahrenheit_readings

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_celsius = [0, 100, -40, 37.5, "invalid"]
    fahrenheit_readings = converter.convert_all(sample_celsius)
    print(fahrenheit_readings)