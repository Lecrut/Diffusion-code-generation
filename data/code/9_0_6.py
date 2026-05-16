import math
def convert_volume(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    conversion_factors = {
        'L': 1.0 / 1000.0,                 
        'mL': 1.0 / 1000000.0,                     
        'm^3': 1.0,
        'gal': 0.00378541,                           
        'in^3': 1.6387e-6                     
    }
    if from_unit in conversion_factors:
        value_in_m3 = value * conversion_factors[from_unit]
    else:
        raise ValueError(f"Unknown source unit: {from_unit}")
    if to_unit in conversion_factors:
        result = value_in_m3 / conversion_factors[to_unit]
        return result
    else:
        raise ValueError(f"Unknown target unit: {to_unit}")
if __name__ == '__main__':
    sample_value = 10
    from_unit = 'L'
    to_unit = 'gal'
    try:
        result = convert_volume(sample_value, from_unit, to_unit)
        print(f"{sample_value} {from_unit} is equal to {result:.4f} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}")
    sample_value_2 = 1000
    from_unit_2 = 'm^3'
    to_unit_2 = 'mL'
    try:
        result_2 = convert_volume(sample_value_2, from_unit_2, to_unit_2)
        print(f"{sample_value_2} {from_unit_2} is equal to {result_2:.0f} {to_unit_2}")
    except ValueError as e:
        print(f"Error: {e}")
    sample_value_3 = 1
    from_unit_3 = 'in^3'
    to_unit_3 = 'L'
    try:
        result_3 = convert_volume(sample_value_3, from_unit_3, to_unit_3)
        print(f"{sample_value_3} {from_unit_3} is equal to {result_3:.6f} {to_unit_3}")
    except ValueError as e:
        print(f"Error: {e}")