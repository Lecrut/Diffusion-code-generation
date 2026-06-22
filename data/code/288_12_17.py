class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32
    
    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9
    
    def kelvin_to_celsius(self, kelvin):
        return kelvin - 273.15

class TemperatureCalculator:
    def __init__(self, converter):
        self.converter = converter
    
    def average_temperature(self, temp1_celsius, temp2_fahrenheit, temp3_kelvin):
        temp2_celsius = self.converter.fahrenheit_to_celsius(temp2_fahrenheit)
        temp3_celsius = self.converter.kelvin_to_celsius(temp3_kelvin)
        return (temp1_celsius + temp2_celsius + temp3_celsius) / 3

if __name__ == '__main__':
    converter = TemperatureConverter()
    calculator = TemperatureCalculator(converter)
    result = calculator.average_temperature(25.0, 68.0, 300.15)
    print(f"The average temperature is {result:.2f}°C")