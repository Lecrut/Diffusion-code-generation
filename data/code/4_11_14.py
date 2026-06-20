def adjust_distance(distance, unit):
    conversion_factors = {
        'miles': 1.60934,
        'km': 0.621371
    }
    if unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    
    if unit == 'miles':
        factor = conversion_factors['miles']
        result = distance * factor
        adjusted_unit = 'km'
    else:
        factor = conversion_factors['km']
        result = distance * factor
        adjusted_unit = 'miles'
    
    print(f"Adjusting {distance} {unit} to {adjusted_unit}")
    print(f"Factor used: {factor}")
    return result

if __name__ == '__main__':
    miles = 10
    km = 16.0934
    print("From miles to km:")
    adjust_distance(miles, 'miles')
    print(f"Result: {adjust_distance(miles, 'miles')} km")
    print()
    print("From km to miles:")
    adjust_distance(km, 'km')
    print(f"Result: {adjust_distance(km, 'km')} miles")