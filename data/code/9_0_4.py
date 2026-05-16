import math
def convert_volume(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    conversion_factors = {
        'L': 1.0 / 1000.0,                 
        'mL': 1.0 / 1000000.0,                      
        'm^3': 1.0,
        'gal': 0.00378541,                           
        'in^3': 1.6387e-5                     
    }
    value_in_m3 = value
    if from_unit == 'L':
        value_in_m3 = value * conversion_factors['L']
    elif from_unit == 'mL':
        value_in_m3 = value * conversion_factors['mL']
    elif from_unit == 'm^3':
        value_in_m3 = value
    elif from_unit == 'gal':
        value_in_m3 = value * conversion_factors['gal']
    elif from_unit == 'in^3':
        value_in_m3 = value * conversion_factors['in^3']
    else:
        raise ValueError("Unsupported 'from_unit'")
    if to_unit == 'L':
        return value_in_m3 / conversion_factors['L']
    elif to_unit == 'mL':
        return value_in_m3 / conversion_factors['mL']
    elif to_unit == 'm^3':
        return value_in_m3
    elif to_unit == 'gal':
        return value_in_m3 / conversion_factors['gal']
    elif to_unit == 'in^3':
        return value_in_m3 / conversion_factors['in^3']
    else:
        raise ValueError("Unsupported 'to_unit'")
def main():
    sample_value = 10.0
    from_unit = 'L'
    to_unit = 'gal'
    print(f"Sample Value: {sample_value} {from_unit}")
    try:
        result = convert_volume(sample_value, from_unit, to_unit)
        print(f"Converted Value: {result:.4f} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == '__main__':
    main()