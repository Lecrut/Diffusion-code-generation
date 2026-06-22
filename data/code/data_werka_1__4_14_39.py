def convert_distance(value, source_unit):
    conversion_factors = {
        'meters': {'kilometers': 0.001, 'miles': 0.000621371, 'feet': 3.28084},
        'kilometers': {'meters': 1000, 'miles': 0.621371, 'feet': 3280.84},
        'miles': {'meters': 1609.34, 'kilometers': 1.60934, 'feet': 5280},
        'feet': {'meters': 0.3048, 'kilometers': 0.0003048, 'miles': 0.000189394}
    }
    
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a numeric type.")
    
    if source_unit not in conversion_factors:
        raise ValueError("Invalid source unit. Choose from 'meters', 'kilometers', 'miles', or 'feet'.")
    
    return round(value, 6)

if __name__ == '__main__':
    sample_values = [
        (1000, 'meters'),
        (5, 'kilometers'),
        (10, 'miles'),
        (3280.84, 'feet')
    ]
    
    for value, unit in sample_values:
        converted_value = convert_distance(value, unit)
        print(f"{value} {unit} is {converted_value:.6f}")