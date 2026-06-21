def validate_temperatures(celsius_list):
    if not isinstance(celsius_list, list):
        raise ValueError("Input must be a list.")
    for temp in celsius_list:
        if not isinstance(temp, (int, float)):
            raise ValueError("All elements in the list must be numbers.")

def convert_temp(celsius_list):
    validate_temperatures(celsius_list)
    conversion_factor = 9 / 5
    base_offset = 32
    return [c * conversion_factor + base_offset for c in celsius_list]

if __name__ == '__main__':
    sample_temps = [-40, 0, 100, 37]
    try:
        fahrenheit_temps = convert_temp(sample_temps)
        print(fahrenheit_temps)
    except ValueError as e:
        print(e)