def validate_unit(unit):
    supported_units = ['miles', 'km']
    if unit not in supported_units:
        raise ValueError("Unsupported unit type")

def convert_distance(distance, from_unit, to_unit):
    conversion_factors = {
        ('miles', 'km'): 1.60934,
        ('km', 'miles'): 1 / 1.60934
    }
    key = (from_unit, to_unit)
    if key not in conversion_factors:
        raise ValueError("Unsupported unit conversion")
    return distance * conversion_factors[key]

def adjust_distance(distance, unit):
    validate_unit(unit)
    new_unit = 'km' if unit == 'miles' else 'miles'
    adjusted_distance = convert_distance(distance, unit, new_unit)
    return adjusted_distance, new_unit

if __name__ == '__main__':
    sample_distance_miles = 6
    adjusted_distance_km, new_unit_km = adjust_distance(sample_distance_miles, 'miles')
    print(f"{sample_distance_miles} miles is {adjusted_distance_km:.2f} {new_unit_km}")
    sample_distance_km = 12
    adjusted_distance_miles, new_unit_miles = adjust_distance(sample_distance_km, 'km')
    print(f"{sample_distance_km} km is {adjusted_distance_miles:.2f} {new_unit_miles}")