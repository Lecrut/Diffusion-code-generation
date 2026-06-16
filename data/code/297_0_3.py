import math
def convert_length(value, from_unit, to_unit):
    if from_unit == 'm':
        if to_unit == 'km':
            return value / 1000
        elif to_unit == 'ft':
            return value * 3.28084
        elif to_unit == 'mi':
            return value / 1609.34
    elif from_unit == 'km':
        if to_unit == 'm':
            return value * 1000
        elif to_unit == 'ft':
            return value * 3280.84
        elif to_unit == 'mi':
            return value
    elif from_unit == 'ft':
        if to_unit == 'm':
            return value / 3.28084
        elif to_unit == 'km':
            return value / 1609.34
        elif to_unit == 'mi':
            return value / 1609.34
    elif from_unit == 'mi':
        if to_unit == 'km':
            return value * 1.60934
        elif to_unit == 'ft':
            return value * 5280
        elif to_unit == 'mi':
            return value
    return None
def convert_mass(value, from_unit, to_unit):
    if from_unit == 'g':
        if to_unit == 'kg':
            return value / 1000
        elif to_unit == 'lb':
            return value * 0.00220462
        elif to_unit == 'oz':
            return value * 0.0352739
    elif from_unit == 'kg':
        if to_unit == 'g':
            return value * 1000
        elif to_unit == 'lb':
            return value * 2.20462
        elif to_unit == 'oz':
            return value * 35.2739
    elif from_unit == 'lb':
        if to_unit == 'kg':
            return value / 2.20462
        elif to_unit == 'g':
            return value * 453.592
        elif to_unit == 'oz':
            return value * 453.592
    elif from_unit == 'oz':
        if to_unit == 'lb':
            return value / 16
        elif to_unit == 'kg':
            return value * 0.0283495
        elif to_unit == 'g':
            return value * 28.3495
    return None
if __name__ == '__main__':
    print("--- Length Conversions ---")
    length_value = 10
    from_unit = 'm'
    to_unit = 'ft'
    result_length = convert_length(length_value, from_unit, to_unit)
    if result_length is not None:
        print(f"{length_value} {from_unit} is equal to {result_length:.4f} {to_unit}")
    length_value = 1
    from_unit = 'mi'
    to_unit = 'km'
    result_length = convert_length(length_value, from_unit, to_unit)
    if result_length is not None:
        print(f"{length_value} {from_unit} is equal to {result_length:.4f} {to_unit}")
    print("\n--- Mass Conversions ---")
    mass_value = 500
    from_unit = 'g'
    to_unit = 'kg'
    result_mass = convert_mass(mass_value, from_unit, to_unit)
    if result_mass is not None:
        print(f"{mass_value} {from_unit} is equal to {result_mass:.4f} {to_unit}")
    mass_value = 10
    from_unit = 'lb'
    to_unit = 'oz'
    result_mass = convert_mass(mass_value, from_unit, to_unit)
    if result_mass is not None:
        print(f"{mass_value} {from_unit} is equal to {result_mass:.4f} {to_unit}")
    mass_value = 2.20462
    from_unit = 'kg'
    to_unit = 'lb'
    result_mass = convert_mass(mass_value, from_unit, to_unit)
    if result_mass is not None:
        print(f"{mass_value} {from_unit} is equal to {result_mass:.4f} {to_unit}")