class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

    def kelvin_to_celsius(self, kelvin):
        return kelvin - 273.15

if __name__ == '__main__':
    converter = TemperatureConverter()
    
    sample_celsius = 100
    sample_fahrenheit = 212
    sample_kelvin = 373.15
    
    print(f"{sample_celsius}C is {converter.celsius_to_fahrenheit(sample_celsius)}F")
    print(f"{sample_fahrenheit}F is {converter.fahrenheit_to_celsius(sample_fahrenheit)}C")
    print(f"{sample_kelvin}K is {converter.kelvin_to_celsius(sample_kelvin)}C")