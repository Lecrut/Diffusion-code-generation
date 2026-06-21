def convert_distance(value, from_unit):
    conversion_factors = {
        'meters_to_kilometers': 1 / 1000,
        'meters_to_miles': 1 / 1609.344,
        'meters_to_feet': 3.28084,
        'kilometers_to_meters': 1000,
        'kilometers_to_miles': 0.621371,
        'kilometers_to_feet': 3280.84,
        'miles_to_meters': 1609.344,
        'miles_to_kilometers': 1 / 0.621371,
        'miles_to_feet': 5280,
        'feet_to_meters': 1 / 3.28084,
        'feet_to_kilometers': 1 / 3280.84,
        'feet_to_miles': 1 / 5280
    }
    
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a numeric type.")
    
    if from_unit not in conversion_factors:
        raise ValueError("Unsupported unit of measurement.")
    
    to_units = {
        'meters': ['kilometers', 'miles', 'feet'],
        'kilometers': ['meters', 'miles', 'feet'],
        'miles': ['meters', 'kilometers', 'feet'],
        'feet': ['meters', 'kilometers', 'miles']
    }
    
    if from_unit not in to_units:
        raise ValueError("Unsupported unit of measurement.")
    
    for to_unit in to_units[from_unit]:
        conversion_key = f"{from_unit}_to_{to_unit}"
        converted_value = value * conversion_factors[conversion_key]
        print(f"{value} {from_unit} is {converted_value:.6f} {to_unit}")

if __name__ == '__main__':
    convert_distance(100, 'meters')
    convert_distance(5, 'kilometers')
    convert_distance(2, 'miles')
    convert_distance(3000, 'feet')