import argparse

UNIT_CONVERSIONS = {
    'mm': 0.001,
    'cm': 0.01,
    'm': 1.0,
    'km': 1000.0,
    'in': 0.0254,
    'ft': 0.3048,
    'yd': 0.9144,
    'mi': 1609.344,
}

def convert_distance(distance, from_unit, to_unit):
    if from_unit not in UNIT_CONVERSIONS:
        raise ValueError(f"Invalid source unit: {from_unit}")
    if to_unit not in UNIT_CONVERSIONS:
        raise ValueError(f"Invalid target unit: {to_unit}")
    
    base_value = distance * UNIT_CONVERSIONS[from_unit]
    return base_value / UNIT_CONVERSIONS[to_unit]

def parse_arguments(args=None):
    parser = argparse.ArgumentParser(description="Convert distance units.")
    parser.add_argument('--distance1', type=float, required=False, default=100)
    parser.add_argument('--distance2', type=float, required=False, default=500)
    parser.add_argument('--unit', type=str, required=False, default='m')
    return parser.parse_args(args)

def process_conversions(distance1, distance2, target_unit):
    result1 = convert_distance(distance1, 'm', target_unit)
    result2 = convert_distance(distance2, 'm', target_unit)
    return {
        f"{distance1} m": result1,
        f"{distance2} m": result2,
    }

if __name__ == '__main__':
    args = parse_arguments()
    try:
        results = process_conversions(args.distance1, args.distance2, args.unit)
        for key, val in results.items():
            print(f"{key} = {val} {args.unit}")
    except ValueError as e:
        print(f"Error: {e}")