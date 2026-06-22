import argparse

UNIT_FACTORS = {
    "m": 1.0,
    "km": 1000.0,
    "cm": 0.01,
    "mm": 0.001,
    "mi": 1609.344,
    "ft": 0.3048,
    "in": 0.0254,
    "yd": 0.9144,
}

def validate_unit(unit):
    if unit not in UNIT_FACTORS:
        raise ValueError(f"Unsupported unit: {unit}. Allowed units are {list(UNIT_FACTORS.keys())}")
    return True

def convert_to_meters(distance, unit):
    validate_unit(unit)
    return distance * UNIT_FACTORS[unit]

def convert_from_meters(meters, unit):
    validate_unit(unit)
    return meters / UNIT_FACTORS[unit]

def process_distances(dist1, dist2, output_unit):
    validate_unit(output_unit)
    meters1 = convert_to_meters(dist1, "m")
    meters2 = convert_to_meters(dist2, "m")
    total_meters = meters1 + meters2
    result = convert_from_meters(total_meters, output_unit)
    return result

def create_parser():
    parser = argparse.ArgumentParser(description="Sum two distances and convert to target unit")
    parser.add_argument("--dist1", type=float, default=0.0, help="First distance value")
    parser.add_argument("--unit1", type=str, default="m", help="Unit of first distance")
    parser.add_argument("--dist2", type=float, default=0.0, help="Second distance value")
    parser.add_argument("--unit2", type=str, default="m", help="Unit of second distance")
    parser.add_argument("--output", type=str, default="m", help="Output unit for result")
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args([])
    
    dist1_val = args.dist1
    unit1_val = args.unit1
    dist2_val = args.dist2
    unit2_val = args.unit2
    output_unit_val = args.output
    
    try:
        validate_unit(unit1_val)
        validate_unit(unit2_val)
        validate_unit(output_unit_val)
        
        m1 = convert_to_meters(dist1_val, unit1_val)
        m2 = convert_to_meters(dist2_val, unit2_val)
        total = m1 + m2
        final_result = convert_from_meters(total, output_unit_val)
        
        print(final_result)
    except ValueError as e:
        print(f"Error: {e}")
        raise

if __name__ == "__main__":
    main()