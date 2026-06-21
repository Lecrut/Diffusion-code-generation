def celsius_to_kelvin(celsius):
    if not isinstance(celsius, (int, float)):
        raise ValueError("Input must be a numeric type.")
    return celsius + 273.15

if __name__ == '__main__':
    sample_values = [-40, 0, 37, 100, 1000]
    for value in sample_values:
        try:
            kelvin_value = celsius_to_kelvin(value)
            print(f"{value}°C is {kelvin_value}K")
        except ValueError as e:
            print(e)