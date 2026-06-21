class TemperatureConverter:
    CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
    FAHRENHEIT_OFFSET = 32

    def convert_all(self, celsius_readings):
        if not isinstance(celsius_readings, list):
            raise ValueError("Input must be a list of Celsius temperatures.")
        
        fahrenheit_readings = []
        for celsius in celsius_readings:
            fahrenheit = self._convert_celsius_to_fahrenheit(celsius)
            fahrenheit_readings.append(fahrenheit)
        
        return fahrenheit_readings

    def _convert_celsius_to_fahrenheit(self, celsius):
        return (celsius * self.CELSIUS_TO_FAHRENHEIT_FACTOR) + self.FAHRENHEIT_OFFSET

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_celsius = [-20, -5, 0, 15, 30, 100]
    fahrenheit_readings = converter.convert_all(sample_celsius)
    print(fahrenheit_readings)