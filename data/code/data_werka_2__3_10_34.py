def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15

if __name__ == '__main__':
    sample_values = [32, 212, -40]
    for value in sample_values:
        kelvin_value = fahrenheit_to_kelvin(value)
        print(f"{value}°F is {kelvin_value:.2f}K")