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
        'celsius': [0, 100],
        'fahrenheit': [-40, 212]
    }
    for c in sample_values['celsius']:
        f = celsius_to_fahrenheit(c)
        k = celsius_to_kelvin(c)
        print(f"C: {c} F: {f:.2f} K: {k:.2f}")
    for f_val in sample_values['fahrenheit']:
        c = fahrenheit_to_celsius(f_val)
        k = kelvin_to_celsius(0) + (kelvin_to_celsius(c))                                                                             
        correct_k = celsius_to_kelvin(correct_c := fahrenheit_to_celsius(f_val))
        print(f"F: {f_val} C: {correct_c:.2f} K: {correct_k:.2f}")
    k_samples = [c + 273.15 for c in sample_values['celsius']]
    for i, (k) in enumerate(k_samples):
        print(f"K Sample {i+1}: K: {k:.2f} C: {kelvin_to_celsius(k):.2f}")