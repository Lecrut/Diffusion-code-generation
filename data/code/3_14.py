def fahrenheit_to_kelvin(fahrenheit):
    celsius = (fahrenheit - 32.0) * 5.0 / 9.0
    kelvin = celsius + 273.15
    return kelvin
if __name__ == '__main__':
    sample_fahrenheit_values = [32.0, 212.0, -459.67, 98.6, 0.0]
    for f_val in sample_fahrenheit_values:
        k_val = fahrenheit_to_kelvin(f_val)
        print(k_val)