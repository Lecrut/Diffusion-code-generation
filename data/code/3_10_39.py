def fahrenheit_to_kelvin(fahrenheit):
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError("Input must be an integer or float")
    return (fahrenheit - 32) * 5.0 / 9.0 + 273.15

if __name__ == '__main__':
    sample_values = [0, 100, -460, 32]
    for value in sample_values:
        try:
            kelvin_value = fahrenheit_to_kelvin(value)
            print(f"{value} Fahrenheit is {kelvin_value:.2f} Kelvin")
        except ValueError as e:
            print(e)