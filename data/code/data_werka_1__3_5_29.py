class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

    def kelvin_to_celsius(self, kelvin):
        return kelvin - 273.15

if __name__ == '__main__':
    converter = TemperatureConverter()
    
    celsius_value = 25
    fahrenheit_value = 77
    kelvin_value = 300
    
    print(f"Celsius to Fahrenheit: {converter.celsius_to_fahrenheit(celsius_value)}")
    print(f"Fahrenheit to Celsius: {converter.fahrenheit_to_celsius(fahrenheit_value)}")
    print(f"Kelvin to Celsius: {converter.kelvin_to_celsius(kelvin_value)}")