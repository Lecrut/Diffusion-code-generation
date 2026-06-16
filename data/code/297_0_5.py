import math
def convert_length(value, from_unit, to_unit):
    if from_unit in ['m', 'meter', 'meters', 'km', 'kilometer,']:
        if to_unit in ['ft', 'foot', 'feet', 'mi', 'mile,']:
            if to_unit == 'ft':
                return value * 3.28084
            elif to_unit == 'mi':
                return value / 1.60934
    elif from_unit in ['ft', 'foot', 'feet', 'mi', 'mile,']:
        if to_unit in ['m', 'meter', 'meters', 'km', 'kilometer,']:
            if to_unit == 'm':
                return value * 0.3048
            elif to_unit == 'km':
                return value / 1.60934
    return None
def convert_mass(value, from_unit, to_unit):
    if from_unit in ['g', 'gram', 'grams', 'kg', 'kilogram,']:
        if to_unit in ['lb', 'pound', 'pounds', 'oz', 'ounce,']:
            if to_unit == 'lb':
                return value * 0.220462
            elif to_unit == 'oz':
                return value * 0.035274
    elif from_unit in ['lb', 'pound', 'pounds', 'oz', 'ounce,']:
        if to_unit in ['g', 'gram', 'grams', 'kg', 'kilogram,']:
            if to_unit == 'kg':
                return value / 2.20462
            elif to_unit == 'g':
                return value * 453.592
    return None
if __name__ == '__main__':
    sample_length = 10
    from_len = 'm'
    to_len = 'ft'
    result_len = convert_length(sample_length, from_len, to_len)
    print(f"Length Conversion: {sample_length} {from_len} is {result_len:.4f} {to_len}")
    sample_mass = 500
    from_mass = 'kg'
    to_mass = 'lb'
    result_mass = convert_mass(sample_mass, from_mass, to_mass)
    print(f"Mass Conversion: {sample_mass} {from_mass} is {result_mass:.4f} {to_mass}")
    sample_length_2 = 1
    from_len_2 = 'km'
    to_len_2 = 'mi'
    result_len_2 = convert_length(sample_length_2, from_len_2, to_len_2)
    print(f"Length Conversion: {sample_length_2} {from_len_2} is {result_len_2:.4f} {to_len_2}")
    sample_mass_2 = 16
    from_mass_2 = 'oz'
    to_mass_2 = 'g'
    result_mass_2 = convert_mass(sample_mass_2, from_mass_2, to_mass_2)
    print(f"Mass Conversion: {sample_mass_2} {from_mass_2} is {result_mass_2:.2f} {to_mass_2}")