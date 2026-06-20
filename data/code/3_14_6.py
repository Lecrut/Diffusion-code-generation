def fahrenheit_to_kelvin(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    kelvin = celsius + 273.15
    return kelvin
if __name__ == '__main__':
    sample_values = [32, 212, -459.67, 100, 0]
    for value in sample_values:
        result = fahrenheit_to_kelvin(value)
        print(result)