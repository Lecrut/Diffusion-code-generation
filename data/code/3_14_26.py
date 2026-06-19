def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5.0/9.0 + 273.15
    return kelvin

if __name__ == '__main__':
    sample_values = [32, 212, -459.67]
    for value in sample_values:
        result = fahrenheit_to_kelvin(value)
        print(f"{value}°F is {result:.2f}K")