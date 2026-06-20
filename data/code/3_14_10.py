def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15

if __name__ == '__main__':
    samples = [32.0, 212.0, 0.0]
    for temp_f in samples:
        result = fahrenheit_to_kelvin(temp_f)
        print(result)