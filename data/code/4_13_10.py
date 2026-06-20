import argparse

UNIT_TO_METERS = {
    'm': 1.0,
    'km': 1000.0,
    'cm': 0.01,
    'mm': 0.001,
    'mi': 1609.34,
    'ft': 0.3048,
    'in': 0.0254,
}

VALID_UNITS = set(UNIT_TO_METERS.keys())

def convert_distance(value, from_unit, to_unit):
    if from_unit not in VALID_UNITS:
        raise ValueError(f"Invalid from_unit: {from_unit}")
    if to_unit not in VALID_UNITS:
        raise ValueError(f"Invalid to_unit: {to_unit}")
    meters = value * UNIT_TO_METERS[from_unit]
    return meters / UNIT_TO_METERS[to_unit]

def main():
    parser = argparse.ArgumentParser(description="Convert distance.")
    parser.add_argument('--distance', type=float, default=10.0)
    parser.add_argument('--from-unit', type=str, default='km')
    parser.add_argument('--to-unit', type=str, default='mi')
    args = parser.parse_args([])
    
    try:
        result = convert_distance(args.distance, args.from_unit, args.to_unit)
        print(result)
    except ValueError as e:
        print(str(e))

if __name__ == '__main__':
    main()