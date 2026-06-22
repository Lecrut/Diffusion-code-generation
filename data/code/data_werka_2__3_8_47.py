def validate_temperature_list(celsius_list):
    if not isinstance(celsius_list, list):
        raise ValueError("Input must be a list.")
    if not all(isinstance(c, (int, float)) for c in celsius_list):
        raise ValueError("All elements in the list must be numbers.")

def celsius_to_fahrenheit(celsius_list):
    validate_temperature_list(celsius_list)
    conversion_factor = 9 / 5
    offset = 32
    return [(c * conversion_factor) + offset for c in celsius_list]

if __name__ == '__main__':
    sample_temperatures = [-40, -10, 0, 10, 20, 100]
    try:
        fahrenheit_temperatures = celsius_to_fahrenheit(sample_temperatures)
        print(fahrenheit_temperatures)
    except ValueError as e:
        print(e)