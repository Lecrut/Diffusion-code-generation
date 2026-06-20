def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15

if __name__ == '__main__':
    sample_values = [32, 212, -40, 98.6, 100]
    for temp in sample_values:
        result = fahrenheit_to_kelvin(temp)
        print(result)