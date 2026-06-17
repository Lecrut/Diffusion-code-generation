import sys
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def celsius_to_kelvin(celsius):
    return celsius + 273.15
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15
def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)
def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)
if __name__ == '__main__':
    sample_celsius = 25.0
    sample_fahrenheit = 77.0
    sample_kelvin = 298.15
    print("--- Temperature Conversion Demonstration ---")
    print(f"\nSample Celsius: {sample_celsius}°C")
    print(f"  To Fahrenheit: {celsius_to_fahrenheit(sample_celsius):.2f}°F")
    print(f"  To Kelvin: {celsius_to_kelvin(sample_celsius):.2f}K")
    print(f"\nSample Fahrenheit: {sample_fahrenheit}°F")
    print(f"  To Celsius: {fahrenheit_to_celsius(sample_fahrenheit):.2f}°C")
    print(f"  To Kelvin: {fahrenheit_to_kelvin(sample_fahrenheit):.2f}K")
    print(f"\nSample Kelvin: {sample_kelvin}K")
    print(f"  To Celsius: {kelvin_to_celsius(sample_kelvin):.2f}°C")
    print(f"  To Fahrenheit: {kelvin_to_fahrenheit(sample_kelvin):.2f}°F")