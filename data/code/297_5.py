def setup_conversion_factors():
    length_factors = {
        'meter_to_foot': 3.28084,
        'foot_to_meter': 0.3048,
        'kilometer_to_meter': 1000,
        'meter_to_kilometer': 0.001,
    }
    mass_factors = {
        'kilogram_to_gram': 1000,
        'gram_to_kilogram': 0.001,
        'pound_to_kilogram': 0.453592,
        'kilogram_to_pound': 2.20462,
    }
    return {
        'length': length_factors,
        'mass': mass_factors
    }
def convert_units(value, from_unit, to_unit, conversion_data):
    if from_unit == to_unit:
        return value
    if from_unit == 'meter' or from_unit == 'foot' or from_unit == 'kilometer':
        if to_unit == 'meter' or to_unit == 'foot' or to_unit == 'kilometer':
            if from_unit == 'meter' and to_unit == 'foot':
                factor = conversion_data['length']['meter_to_foot']
            elif from_unit == 'foot' and to_unit == 'meter':
                factor = conversion_data['length']['foot_to_meter']
            elif from_unit == 'kilometer' and to_unit == 'meter':
                factor = conversion_data['length']['kilometer_to_meter']
            elif from_unit == 'meter' and to_unit == 'kilometer':
                factor = conversion_data['length']['meter_to_kilometer']
            elif from_unit == 'kilometer' and to_unit == 'meter':
                factor = conversion_data['length']['meter_to_kilometer']
            elif from_unit == 'foot' and to_unit == 'kilometer':
                factor = conversion_data['length']['foot_to_meter'] * conversion_data['length']['kilometer_to_meter']
            elif from_unit == 'kilometer' and to_unit == 'foot':
                factor = conversion_data['length']['kilometer_to_meter'] / conversion_data['length']['foot_to_meter']
            else:
                return None
            return value * factor
    elif from_unit == 'kilogram' or from_unit == 'gram' or from_unit == 'pound':
        if to_unit == 'kilogram' or to_unit == 'gram' or to_unit == 'pound':
            if from_unit == 'kilogram' and to_unit == 'gram':
                factor = conversion_data['mass']['kilogram_to_gram']
            elif from_unit == 'gram' and to_unit == 'kilogram':
                factor = conversion_data['mass']['gram_to_kilogram']
            elif from_unit == 'pound' and to_unit == 'kilogram':
                factor = conversion_data['mass']['pound_to_kilogram']
            elif from_unit == 'kilogram' and to_unit == 'pound':
                factor = conversion_data['mass']['kilogram_to_pound']
            elif from_unit == 'gram' and to_unit == 'pound':
                factor = conversion_data['mass']['gram_to_kilogram'] * conversion_data['mass']['kilogram_to_pound']
            elif from_unit == 'pound' and to_unit == 'gram':
                factor = conversion_data['mass']['pound_to_kilogram'] * conversion_data['mass']['kilogram_to_gram']
            else:
                return None
            return value * factor
    return None
if __name__ == '__main__':
    conversion_data = setup_conversion_factors()
    print("--- Length Conversions ---")
    value1 = 10
    from_unit1 = 'meter'
    to_unit1 = 'foot'
    result1 = convert_units(value1, from_unit1, to_unit1, conversion_data)
    print(f"{value1} meters is {result1} feet")
    value2 = 5
    from_unit2 = 'foot'
    to_unit2 = 'meter'
    result2 = convert_units(value2, from_unit2, to_unit2, conversion_data)
    print(f"{value2} feet is {result2} meters")
    value3 = 2.5
    from_unit3 = 'kilometer'
    to_unit3 = 'meter'
    result3 = convert_units(value3, from_unit3, to_unit3, conversion_data)
    print(f"{value3} kilometers is {result3} meters")
    print("\n--- Mass Conversions ---")
    value4 = 2
    from_unit4 = 'kilogram'
    to_unit4 = 'gram'
    result4 = convert_units(value4, from_unit4, to_unit4, conversion_data)
    print(f"{value4} kilograms is {result4} grams")
    value5 = 10
    from_unit5 = 'pound'
    to_unit5 = 'kilogram'
    result5 = convert_units(value5, from_unit5, to_unit5, conversion_data)
    print(f"{value5} pounds is {result5} kilograms")
    value6 = 1000
    from_unit6 = 'gram'
    to_unit6 = 'pound'
    result6 = convert_units(value6, from_unit6, to_unit6, conversion_data)
    print(f"{value6} grams is {result6} pounds")