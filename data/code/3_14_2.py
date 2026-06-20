def fahrenheit_to_kelvin(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    kelvin = celsius + 273.15
    return kelvin
if __name__ == '__main__':
    sample_fahrenheit_values = [32, 212, -459.67, 68, 98.6]
    for f in sample_fahrenheit_values:
        k = fahrenheit_to_kelvin(f)
        print(k)