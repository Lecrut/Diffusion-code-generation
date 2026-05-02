import math
def convert_volume(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    conversion_factors = {
        'L': 0.001,                       
        'mL': 0.000001,                               
        'm^3': 1.0,
        'gal': 0.00378541,                                
        'in^3': 0.0000163871,                                   
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
    sample_from_unit = 'L'
    sample_to_unit = 'gal'
    print(f"Sample Value: {sample_value} {sample_from_unit}")
    try:
        result = convert_volume(sample_value, sample_from_unit, sample_to_unit)
        print(f"Converted Value: {result:.4f} {sample_to_unit}")
    except ValueError as e:
        print(f"Error during conversion: {e}")
    print("-" * 20)
    sample_value_2 = 500
    sample_from_unit_2 = 'mL'
    sample_to_unit_2 = 'in^3'
    print(f"Sample Value: {sample_value_2} {sample_from_unit_2}")
    try:
        result_2 = convert_volume(sample_value_2, sample_from_unit_2, sample_to_unit_2)
        print(f"Converted Value: {result_2:.6f} {sample_to_unit_2}")
    except ValueError as e:
        print(f"Error during conversion: {e}")
    print("-" * 20)
    sample_value_3 = 1
    sample_from_unit_3 = 'm^3'
    sample_to_unit_3 = 'L'
    print(f"Sample Value: {sample_value_3} {sample_from_unit_3}")
    try:
        result_3 = convert_volume(sample_value_3, sample_from_unit_3, sample_to_unit_3)
        print(f"Converted Value: {result_3:.4f} {sample_to_unit_3}")
    except ValueError as e:
        print(f"Error during conversion: {e}")