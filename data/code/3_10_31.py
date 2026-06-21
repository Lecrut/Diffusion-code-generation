def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0 + 273.15

if __name__ == '__main__':
    sample_values = [32, 212, -40, 100]
    for value in sample_values:
        kelvin_value = fahrenheit_to_kelvin(value)
        print(f"{value} Fahrenheit is {kelvin_value:.2f} Kelvin")