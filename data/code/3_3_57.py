def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kelvin_to_celsius(kelvin):
    if kelvin < 0:
        raise ValueError("Kelvin temperature cannot be below absolute zero")
    return kelvin - 273.15

class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        return celsius_to_fahrenheit(celsius)

    def fahrenheit_to_celsius(self, fahrenheit):
        return fahrenheit_to_celsius(fahrenheit)

    def kelvin_to_celsius(self, kelvin):
        return kelvin_to_celsius(kelvin)

if __name__ == '__main__':
    sample_celsius = 30
    sample_fahrenheit = 86
    sample_kelvin = 303.15

    converter = TemperatureConverter()
    
    print(f"{sample_celsius}C is {converter.celsius_to_fahrenheit(sample_celsius)}F")
    print(f"{sample_fahrenheit}F is {converter.fahrenheit_to_celsius(sample_fahrenheit)}C")
    print(f"{sample_kelvin}K is {converter.kelvin_to_celsius(sample_kelvin)}C")