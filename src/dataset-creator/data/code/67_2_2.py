from typing import List, Optional
def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9 / 5) + 32
def fahrenheit_to_celsius(f: float) -> float:
    return ((f - 32) * 5) / 9
def celsius_to_kelvin(c: float) -> float:
    return c + 273.15
def kelvin_to_celsius(k: float) -> float:
    return k - 273.15
def fahrenheit_to_kelvin(f: float) -> float:
    return ((f - 32) * 5 / 9) + 273.15
if __name__ == '__main__':
    sample_celsius = [0, 100]
    sample_fahrenheit = [-40, 212]
    print("Celsius to Fahrenheit:")
    for c in sample_celsius:
        f = celsius_to_fahrenheit(c)
        print(f"{c}°C -> {f:.2f}°F")
    print("\nCelsius to Kelvin:")
    for c in sample_celsius:
        k = celsius_to_kelvin(c)
        print(f"{c}°C -> {k:.2f}K")
    print("\nFahrenheit to Celsius:")
    for f_val in sample_fahrenheit:
        c = fahrenheit_to_celsius(f_val)
        print(f"{f_val}°F -> {c:.2f}°C")
    print("\nKelvin to Celsius:")
    k_samples = [0, 373.15]
    for k in k_samples:
        c = kelvin_to_celsius(k)
        print(f"{k}K -> {c:.2f}°C")