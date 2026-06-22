import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Convert distance between units.")
    parser.add_argument("distance1", type=float, help="First distance value.")
    parser.add_argument("distance2", type=float, help="Second distance value.")
    parser.add_argument("output_unit", type=str, choices=["meters", "kilometers", "miles", "feet"], help="Desired output unit.")
    return parser.parse_args()

def convert_distance(value, from_unit, to_unit):
    meters = 0.0
    if from_unit == "meters":
        meters = value
    elif from_unit == "kilometers":
        meters = value * 1000
    elif from_unit == "miles":
        meters = value * 1609.344
    elif from_unit == "feet":
        meters = value * 0.3048
    
    result = 0.0
    if to_unit == "meters":
        result = meters
    elif to_unit == "kilometers":
        result = meters / 1000
    elif to_unit == "miles":
        result = meters / 1609.344
    elif to_unit == "feet":
        result = meters / 0.3048
    return result

def main():
    args = parse_arguments()
    
    total_meters = 0.0
    if args.distance1 > 0:
        total_meters += convert_distance(args.distance1, args.output_unit, args.output_unit)
    
    if args.distance2 > 0:
        total_meters += convert_distance(args.distance2, args.output_unit, args.output_unit)
        
    final_result = total_meters
    print(final_result)

if __name__ == '__main__':
    main()