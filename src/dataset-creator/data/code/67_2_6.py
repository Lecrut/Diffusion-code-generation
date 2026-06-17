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
    sample_values = [0, 100]
    for c in sample_values:
        f_temp = celsius_to_fahrenheit(c)
        k_temp = celsius_to_kelvin(c)
        print(f"Celsius {c} -> Fahrenheit {f_temp:.2f}")
        print(f"Celsius {c} -> Kelvin {k_temp:.2f}\n")
    for f in sample_values:
        c_temp = fahrenheit_to_celsius(f)
        k_temp = kelvin_to_celsius(c + 273.15 if (c := fahrenheit_to_celsius(f)) else None)
        print(f"Fahrenheit {f} -> Celsius {c:.2f}")