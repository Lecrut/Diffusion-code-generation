import sys
def convert_to_km(value, unit):
    conversion_factors = {
        'm': 0.001,
        'km': 1.0,
        'mi': 1.60934,
        'yd': 0.00067108,
        'ft': 0.0003048,
        'in': 0.0000168938
    }
    if unit in conversion_factors:
        return value * conversion_factors[unit]
    else:
        raise ValueError(f"Unsupported unit: {unit}")
if __name__ == '__main__':
    sample_distances = [
        (100, 'm'),
        (5, 'mi'),
        (10, 'km'),
        (1000, 'ft')
    ]
    for distance, unit in sample_distances:
        try:
            result_km = convert_to_km(distance, unit)
            print(f"Input: {distance} {unit}")
            print(f"Result (km): {result_km}")
            print("-" * 20)
        except ValueError as e:
            print(f"Error processing sample: {e}", file=sys.stderr)
        except Exception as e:
            print(f"An unexpected error occurred: {e}", file=sys.stderr)