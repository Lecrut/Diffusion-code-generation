conversion_factors = {
    'to_km': 1.60934,
    'to_miles': 0.621371
}

def convert_distance(distance, unit):
    if unit not in conversion_factors:
        raise ValueError("Invalid unit specified. Use 'to_km' or 'to_miles'.")
    return distance * conversion_factors[unit]

if __name__ == '__main__':
    sample_distance = 100
    sample_unit = 'to_km'
    try:
        distance_value = float(sample_distance)
        if sample_unit == 'to_km':
            result = convert_distance(distance_value, 'to_miles')
            print(f"Original distance: {sample_distance} kilometers")
            print(f"Converted distance: {result:.2f} miles")
        elif sample_unit == 'to_miles':
            result = convert_distance(distance_value, 'to_km')
            print(f"Original distance: {sample_distance} miles")
            print(f"Converted distance: {result:.2f} kilometers")
    except ValueError as e:
        print(f"Error: Invalid input provided. Details: {e}", file=sys.stderr)