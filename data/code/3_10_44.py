def fahrenheit_to_kelvin(fahrenheit):
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError("Input must be a number")
    return (fahrenheit - 32) * 5 / 9 + 273.15

if __name__ == '__main__':
    sample_values = [0, 100, 32, -40]
    for value in sample_values:
        try:
            kelvin_value = fahrenheit_to_kelvin(value)
            print(f"{value}°F is {kelvin_value:.2f}K")
        except ValueError as e:
            print(e)