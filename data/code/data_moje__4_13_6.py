import argparse
import sys

def convert_distances(dist1, dist2, target_unit):
    units = ['km', 'm', 'cm', 'mm', 'mi', 'ft', 'in']
    if target_unit not in units:
        raise ValueError(f"Invalid unit '{target_unit}'. Must be one of: {units}")
    
    unit_to_meters = {
        'km': 1000,
        'm': 1,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.34,
        'ft': 0.3048,
        'in': 0.0254
    }
    
    dist1_m = dist1 * unit_to_meters.get(dist1_unit, 0)
    dist2_m = dist2 * unit_to_meters.get(dist2_unit, 0)
    total_m = dist1_m + dist2_m
    return total_m / unit_to_meters[target_unit]

def main():
    parser = argparse.ArgumentParser(description="Convert sum of two distances to a target unit.")
    parser.add_argument('distance1', type=float, help="First distance value")
    parser.add_argument('unit1', type=str, help="Unit for first distance")
    parser.add_argument('distance2', type=float, help="Second distance value")
    parser.add_argument('unit2', type=str, help="Unit for second distance")
    parser.add_argument('target_unit', type=str, help="Desired output unit")
    
    args = parser.parse_args()
    
    try:
        result = convert_distances(args.distance1, args.distance2, args.target_unit)
        print(f"{result:.2f} {args.target_unit}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    sys.argv = ['script_name', '1.5', 'km', '500', 'm', 'mi']
    main()