from typing import Union
def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9 / 5) + 32
def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5 / 9
def celsius_to_kelvin(c: float) -> float:
    return c + 273.15
def kelvin_to_celsius(k: float) -> float:
    return k - 273.15
if __name__ == '__main__':
    sample_values = {
        'celsius_0': (0, celsius_to_fahrenheit(0), fahrenheit_to_celsius(0), kelvin_to_celsius(celsius_to_kelvin(0))),
        'fahrenheit_32': (32, celsius_to_fahrenheit(fahrenheit_to_celsius(32)), 32, celsius_to_kelvin(fahrenheit_to_celsius(32))),
    }
    for label, result in sample_values.items():
        print(f"{label}: {result}")