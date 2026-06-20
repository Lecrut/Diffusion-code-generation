def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    celsius = (fahrenheit - 32.0) * 5.0 / 9.0
    return celsius + 273.15

if __name__ == "__main__":
    sample_fahrenheit_values = [32.0, 212.0, -459.67, 100.0, 0.0]
    for f_val in sample_fahrenheit_values:
        k_val = fahrenheit_to_kelvin(f_val)
        print(k_val)