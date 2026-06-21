def celsius_to_kelvin(celsius):
    KELVIN_OFFSET = 273.15
    if celsius < -KELVIN_OFFSET:
        raise ValueError("Temperature in Celsius cannot be less than absolute zero.")
    return celsius + KELVIN_OFFSET

if __name__ == '__main__':
    sample_values = [0, -40, 100, 25.5, 37]
    for value in sample_values:
        try:
            print(f"{value}°C is {celsius_to_kelvin(value)}K")
        except ValueError as e:
            print(e)