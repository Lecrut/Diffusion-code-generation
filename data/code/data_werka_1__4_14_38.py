def convert_distance(value, from_unit):
    conversion_factors = {
        'meters_to_kilometers': 0.001,
        'meters_to_miles': 0.000621371,
        'meters_to_feet': 3.28084,
        'kilometers_to_meters': 1000,
        'kilometers_to_miles': 0.621371,
        'kilometers_to_feet': 3280.84,
        'miles_to_meters': 1609.34,
        'miles_to_kilometers': 1.60934,
        'miles_to_feet': 5280,
        'feet_to_meters': 0.3048,
        'feet_to_kilometers': 0.0003048,
        'feet_to_miles': 0.000189394
    }
    
    valid_units = ['meters', 'kilometers', 'miles', 'feet']
    
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a numeric type.")
    
    if from_unit not in valid_units:
        raise ValueError(f"Invalid unit: {from_unit}. Valid units are: {', '.join(valid_units)}.")
    
    to_units = {
        'meters': ['kilometers', 'miles', 'feet'],
        'kilometers': ['meters', 'miles', 'feet'],
        'miles': ['meters', 'kilometers', 'feet'],
        'feet': ['meters', 'kilometers', 'miles']
    }
    
    results = {}
    for to_unit in to_units[from_unit]:
        conversion_key = f"{from_unit}_to_{to_unit}"
        converted_value = value * conversion_factors[conversion_key]
        results[to_unit] = round(converted_value, 6)
    
    return results

if __name__ == '__main__':
    sample_values = [
        (100, 'meters'),
        (5, 'kilometers'),
        (2.5, 'miles'),
        (3000, 'feet')
    ]
    
    for value, unit in sample_values:
        print(f"Converting {value} {unit}:")
        print(convert_distance(value, unit))
        print()