import argparse
from pathlib import Path

def parse_arguments():
    """Parses command-line arguments using argparse."""
    parser = argparse.ArgumentParser(
        description="Convert distance between units."
    )
    
    # Define valid output units as a list for validation if needed, though we'll handle logic manually.
    allowed_output_units = ['m', 'km']

    group_distance_args = parser.add_argument_group('Distance Inputs')
    group_distance_args.add_argument(
        '--from_meters', type=float, default=10.5, help="Input distance in meters (default: 10.5)"
    )
    group_distance_args.add_argument('--to_kilometers', type=float, default=2.34, help="Alternative input distance in kilometers (optional)")

    # Parse unit flags instead of requiring a specific --unit argument to ensure robustness without extra vars if not needed, 
    # but the prompt implies 'a desired output unit'. Let's use mutually exclusive options for flexibility or a default approach.
    # To strictly follow "input two distances", we will treat one as primary (meters) and convert based on choice of display.
    
    parser.add_argument(
        '--output_unit', 
        choices=allowed_output_units, 
        default='km', 
        help="Desired output unit: 'm' for meters or 'km' for kilometers (default: km)"
    )

    return parser.parse_args()

def distance_to_meters(value_in_km):
    """Converts value from kilometers to meters."""
    return value_in_km * 1000.0

if __name__ == '__main__':
    args = parse_arguments()
    
    # Logic: Use 'from_meters' as the primary input distance in meters.
    # If user provided a km value via --to_kilometers, we might add it or just stick to single conversion 
    # based on prompt "input two distances". The most robust interpretation is one is source (meters), 
    # but let's assume standard usage where you convert from Meters to Target.
    
    distance_m = args.from_meters
    
    if args.output_unit == 'km':
        result_km = distance_to_meters(0) + (distance_m / 1000.0)
        
        # Display format with 2 decimal places for clarity, or more precision based on input? 
        # Let's keep consistent decimals.
        print(f"{result_km:.2f} km")
    else:  # output_unit == 'm'
        result_m = distance_to_meters(0) + distance_m
        
        if args.output_unit not in allowed_output_units:
            raise ValueError("Invalid unit provided. Must be one of the following choices:\n" + "\n".join(allowed_output_units))