import sys
def convert_to_km(value, unit):
    conversion_factors = {
        'm': 0.001,
        'km': 1.0,
        'cm': 0.00001,
        'mm': 0.000001,
        'mi': 1.60934,
        'yd': 0.9144,
        'ft': 0.3048,
        'in': 0.0254
    }
    if unit in conversion_factors:
        return value * conversion_factors[unit]
    else:
        raise ValueError(f"Unsupported unit: {unit}")
def main():
    sample_distances = [
        (100, 'm'),
        (5, 'mi'),
        (100000, 'cm'),
        (1, 'km'),
        (10, 'ft')
    ]
    for distance, unit in sample_distances:
        try:
            result = convert_to_km(distance, unit)
            print(f"Input Distance: {distance} {unit}")
            print(f"Result in Kilometers: {result:.6f} km")
            print("-" * 20)
        except ValueError as e:
            print(f"Error processing sample: {e}", file=sys.stderr)
        except Exception as e:
            print(f"An unexpected error occurred: {e}", file=sys.stderr)
if __name__ == '__main__':
    main()