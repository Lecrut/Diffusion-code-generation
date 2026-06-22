import argparse
import sys

def convert_distances(distance1, distance2, output_unit):
    valid_units = ['km', 'm', 'cm', 'mm', 'mi', 'yd', 'ft', 'in']
    if output_unit not in valid_units:
        raise ValueError(f"Invalid unit: {output_unit}. Must be one of {valid_units}")
    
    unit_to_meters = {
        'km': 1000.0,
        'm': 1.0,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.344,
        'yd': 0.9144,
        'ft': 0.3048,
        'in': 0.0254
    }
    
    meter_to_unit = {v: k for k, v in unit_to_meters.items()}
    
    m1 = distance1 * unit_to_meters[output_unit]
    m2 = distance2 * unit_to_meters[output_unit]
    
    total_meters = m1 + m2
    result = total_meters / unit_to_meters[output_unit]
    
    return result

def main():
    parser = argparse.ArgumentParser(description="Convert and sum two distances.")
    parser.add_argument("distance1", type=float, help="First distance value")
    parser.add_argument("distance2", type=float, help="Second distance value")
    parser.add_argument("unit", type=str, help="Desired output unit")
    
    args = parser.parse_args()
    
    try:
        result = convert_distances(args.distance1, args.distance2, args.unit)
        print(f"{result} {args.unit}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    import sys
    sys.argv = ['script.py', '10', '5', 'km']
    main()