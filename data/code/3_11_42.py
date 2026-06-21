def validate_temperature_list(temperature_list):
    if not isinstance(temperature_list, list):
        raise ValueError("Input must be a list.")
    for temp in temperature_list:
        if not isinstance(temp, (int, float)):
            raise ValueError("All elements in the list must be integers or floats.")

def celsius_to_fahrenheit(celsius_list):
    validate_temperature_list(celsius_list)
    conversion_factor = 9 / 5
    base_temperature = 32
    return [c * conversion_factor + base_temperature for c in celsius_list]

if __name__ == '__main__':
    sample_temperatures = [30, -10, 100, 25]
    try:
        fahrenheit_temperatures = celsius_to_fahrenheit(sample_temperatures)
        print(fahrenheit_temperatures)
    except ValueError as e:
        print(e)