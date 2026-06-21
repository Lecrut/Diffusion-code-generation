def convert_distance(distance, from_unit, to_unit):
    conversion_factors = {
        ('miles', 'kilometers'): 1.60934,
        ('kilometers', 'miles'): 0.621371,
    }
    
    if (from_unit, to_unit) not in conversion_factors:
        raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")
    
    return distance * conversion_factors[(from_unit, to_unit)]

if __name__ == '__main__':
    sample_distances = [
        {'distance': 5, 'from_unit': 'miles', 'to_unit': 'kilometers'},
        {'distance': 10, 'from_unit': 'kilometers', 'to_unit': 'miles'}
    ]
    
    for entry in sample_distances:
        converted_distance = convert_distance(entry['distance'], entry['from_unit'], entry['to_unit'])
        print(f"{entry['distance']} {entry['from_unit']} is {converted_distance:.2f} {entry['to_unit']}")