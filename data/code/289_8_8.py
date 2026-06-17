import sys
def convert_to_kilometers(value, unit):
    conversion_factors = {
        'm': 0.001,
        'km': 1.0,
        'mi': 1.60934,
        'yd': 0.00067108,
        'ft': 0.0003048,
        'in': 0.0000254,
    }
    if unit in conversion_factors:
        return value * conversion_factors[unit]
    else:
        raise ValueError(f"Unsupported unit: {unit}")
def main():
    sample_distances = [
        (1000, 'm'),
        (5, 'mi'),
        (10, 'km'),
        (3000, 'ft'),
        (1200000, 'yd')
    ]
    for distance, unit in sample_distances:
        try:
            result = convert_to_kilometers(distance, unit)
            print(f"Input Distance: {distance} {unit}")
            print(f"Result in Kilometers: {result:.4f} km")
            print("-" * 20)
        except ValueError as e:
            print(f"Error processing sample: {e}", file=sys.stderr)
if __name__ == '__main__':
    main()