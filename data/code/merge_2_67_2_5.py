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
        'celsius_0': (0, celsius_to_fahrenheit(0), kelvin_to_celsius(273.15)),
        'fahrenheit_98': (98, fahrenheit_to_celsius(98), 37.0 + 273.15),
    }
    for label, input_val in sample_values.items():
        c = input_val[0] if isinstance(input_val[0], float) else input_val[0]
        result_f = fahrenheit_to_celsius(c)
        result_k = kelvin_to_celsius(result_f + 273.15)
        print(f"{label}: {c}°C -> {result_f:.2f}°F -> {result_k:.2f}K")