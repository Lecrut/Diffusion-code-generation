import math
def convert_to_base(value, unit):
    conversions = {
        'length': {'meter': 1.0, 'kilometer': 1000.0, 'mile': 1609.34},
        'mass': {'kilogram': 1.0, 'gram': 0.001, 'pound': 0.453592},
        'volume': {'liter': 0.001, 'gallon': 3.78541},
        'temperature': {'celsius': 1.0, 'fahrenheit': 1.8, 'kelvin': 1.8}
    }
    if unit == 'meter':
        return value
    elif unit == 'kilometer':
        return value * 1000.0
    elif unit == 'mile':
        return value * 1609.34
    elif unit == 'gram':
        return value * 0.001
    elif unit == 'pound':
        return value * 0.453592
    elif unit == 'liter':
        return value * 0.001
    elif unit == 'gallon':
        return value * 3.78541
    elif unit == 'celsius':
        return value
    elif unit == 'fahrenheit':
        return (value - 32) * 5/9
    elif unit == 'kelvin':
        return value - 273.15
    else:
        return value
if __name__ == '__main__':
    print("--- Length Conversion ---")
    length_value = 500
    length_unit = "kilometer"
    result_length = convert_to_base(length_value, length_unit)
    print(f"{length_value} {length_unit} is equal to {result_length} meter(s)")
    length_value = 10
    length_unit = "mile"
    result_length = convert_to_base(length_value, length_unit)
    print(f"{length_value} {length_unit} is equal to {result_length} meter(s)")
    print("\n--- Mass Conversion ---")
    mass_value = 2500
    mass_unit = "gram"
    result_mass = convert_to_base(mass_value, mass_unit)
    print(f"{mass_value} {mass_unit} is equal to {result_mass} kilogram(s)")
    mass_value = 5
    mass_unit = "pound"
    result_mass = convert_to_base(mass_value, mass_unit)
    print(f"{mass_value} {mass_unit} is equal to {result_mass} kilogram(s)")
    print("\n--- Volume Conversion ---")
    volume_value = 2
    volume_unit = "gallon"
    result_volume = convert_to_base(volume_value, volume_unit)
    print(f"{volume_value} {volume_unit} is equal to {result_volume} liter(s)")
    print("\n--- Temperature Conversion ---")
    temp_value = 32
    temp_unit = "fahrenheit"
    result_temp = convert_to_base(temp_value, temp_unit)
    print(f"{temp_value} {temp_unit} is equal to {result_temp} celsius")
    temp_value = 273.15
    temp_unit = "kelvin"
    result_temp = convert_to_base(temp_value, temp_unit)
    print(f"{temp_value} {temp_unit} is equal to {result_temp} celsius")