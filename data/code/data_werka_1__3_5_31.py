class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

    def kelvin_to_celsius(self, kelvin):
        return kelvin - 273.15

if __name__ == '__main__':
    converter = TemperatureConverter()
    
    celsius_sample = 25
    fahrenheit_sample = 77
    kelvin_sample = 300
    
    print(f"Celsius to Fahrenheit: {converter.celsius_to_fahrenheit(celsius_sample)}")
    print(f"Fahrenheit to Celsius: {converter.fahrenheit_to_celsius(fahrenheit_sample)}")
    print(f"Kelvin to Celsius: {converter.kelvin_to_celsius(kelvin_sample)}")