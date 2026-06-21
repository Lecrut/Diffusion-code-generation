def celsius_to_kelvin(celsius):
    if not isinstance(celsius, (int, float)):
        raise ValueError("Temperature must be a number")
    return celsius + 273.15

if __name__ == '__main__':
    sample_values = [-40, 0, 25.5, 100, 37]
    for value in sample_values:
        print(f"{value}C is {celsius_to_kelvin(value)}K")