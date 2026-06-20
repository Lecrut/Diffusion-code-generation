import argparse

DISTANCE_TO_METERS = {
    'km': 1000.0,
    'm': 1.0,
    'cm': 0.01,
    'mm': 0.001,
    'mi': 1609.344,
    'yd': 0.9144,
    'ft': 0.3048,
    'in': 0.0254,
}

def calculate_total_distance(dist1, dist2, unit):
    if unit not in DISTANCE_TO_METERS:
        raise ValueError(f"Unsupported unit: {unit}")
    return dist1 + dist2

def convert_unit(total_meters, target_unit):
    if target_unit not in DISTANCE_TO_METERS:
        raise ValueError(f"Unsupported output unit: {target_unit}")
    return total_meters / DISTANCE_TO_METERS[target_unit]

def process_distances(d1, d2, output_unit):
    base_units = list(DISTANCE_TO_METERS.keys())
    total_meters = calculate_total_distance(d1, d2, 'm')
    result = convert_unit(total_meters, output_unit)
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert distances")
    parser.add_argument("--d1", type=float, default=10.0)
    parser.add_argument("--d2", type=float, default=5.0)
    parser.add_argument("--unit", type=str, default="km")
    args = parser.parse_args()
    result = process_distances(args.d1, args.d2, args.unit)
    print(result)