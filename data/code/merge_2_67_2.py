from typing import Optional
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
        "celsius": [0, 100],
        "fahrenheit": [-40, 212],
        "kelvin": [273.15, 373.15]
    }
    for temp_type in ["C", "F"]:
        if temp_type == "C":
            celsius_values = sample_values["celsius"]
            fahrenheit_results = []
            kelvin_results = []
            for c_val in celsius_values:
                f_result = celsius_to_fahrenheit(c_val)
                k_result = celsius_to_kelvin(c_val)
                print(f"{temp_type} {c_val:.2f} -> F: {f_result:.2f}, K: {k_result:.2f}")
            for i, f_val in enumerate(sample_values["fahrenheit"]):
                k_result = celsius_to_kelvin(fahrenheit_to_celsius(f_val))
                print(f"F{sample_values['fahrenheit'][i]:.2f} -> C: {celsius_to_fahrenheit(kelvin_to_celsius(celsius_to_kelvin(0))):.2f}, K: {k_result:.2f}")
        elif temp_type == "F":
            fahrenheit_values = sample_values["fahrenheit"]
            celsius_results = []
            for f_val in fahrenheit_values:
                c_result = fahrenheit_to_celsius(f_val)
                print(f"F{sample_values['fahrenheit'][i]:.2f} -> C: {c_result:.2f}")
        elif temp_type == "K":
            kelvin_values = sample_values["kelvin"]
            for k_val in kelvin_values:
                c_result = kelvin_to_celsius(k_val)
                print(f"K{sample_values['kelvin'][i]:.2f} -> C: {c_result:.2f}")
    test_cases = [0, 100]
    for t in test_cases:
        celsius_to_fahrenheit(t)