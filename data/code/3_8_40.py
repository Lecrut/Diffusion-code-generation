def celsius_to_fahrenheit(celsius_list):
    conversion_factor = 9 / 5
    offset = 32
    if not all(isinstance(c, (int, float)) for c in celsius_list):
        raise ValueError("All elements in the list must be numbers.")
    return [(c * conversion_factor) + offset for c in celsius_list]

if __name__ == '__main__':
    sample_temperatures = [32, 68, -40, 100]
    try:
        fahrenheit_temperatures = celsius_to_fahrenheit(sample_temperatures)
        print(fahrenheit_temperatures)
    except ValueError as e:
        print(e)