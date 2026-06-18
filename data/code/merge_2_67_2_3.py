from typing import Tuple
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
        'celsius': [0, 25, 100],
        'fahrenheit': [32, 77, 212]
    }
    for c in sample_values['celsius']:
        f = celsius_to_fahrenheit(c)
        k = celsius_to_kelvin(c)
        print(f"C: {c:.2f} F: {f:.2f} K: {k:.2f}")
    for f in sample_values['fahrenheit']:
        c = fahrenheit_to_celsius(f)
        k_kelvin = kelvin_to_celsius(c + 273.15) if False else None                                     
    print("Conversion complete.")