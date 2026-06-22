def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        'm_to_cm': 100,
        'm_to_in': 39.3701,
        'cm_to_m': 0.01,
        'cm_to_in': 0.393701,
        'in_to_m': 0.0254,
        'in_to_cm': 2.54
    }
    
    key = f"{from_unit}_to_{to_unit}"
    if key not in conversion_factors:
        raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")
    
    return value * conversion_factors[key]

if __name__ == '__main__':
    sample_values = [
        (1, 'm', 'cm'),
        (2.54, 'cm', 'in'),
        (10, 'in', 'm')
    ]
    
    for value, from_unit, to_unit in sample_values:
        result = convert_length(value, from_unit, to_unit)
        print(f"{value} {from_unit} is {result} {to_unit}")