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
        'celsius': [0, 100],
        'fahrenheit': [32, 212],
        'kelvin': [273.15, 373.15]
    }
    for label in ['Celsius', 'Fahrenheit', 'Kelvin']:
        if label == 'Celsius':
            val = sample_values['celsius'][0]
            print(f"{label} {val}:")
            print(f"  -> Fahrenheit: {fahrenheit_to_celsius(val)} (error)")                                                                                    
        elif label == 'Fahrenheit':
            val = sample_values['fahrenheit'][0]
            c_val = fahrenheit_to_celsius(val)
            k_val = celsius_to_kelvin(c_val)
            print(f"{label} {val}:")
            print(f"  -> Celsius: {c_val}")
            print(f"  -> Kelvin: {k_val}")
        elif label == 'Kelvin':
            val = sample_values['kelvin'][0]
            c_val = kelvin_to_celsius(val)
            f_val = celsius_to_fahrenheit(c_val)
            print(f"{label} {val}:")
            print(f"  -> Celsius: {c_val}")
            print(f"  -> Fahrenheit: {f_val}")