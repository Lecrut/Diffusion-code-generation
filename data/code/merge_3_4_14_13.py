import argparse

def convert_distance(distance: float, unit_in: str, unit_out: str) -> tuple[float, bool]:
    """Converts distance from one unit to another with error handling."""
    
    valid_units = ['km', 'm', 'cm', 'mm']
    
    if unit_in not in valid_units or unit_out not in valid_units:
        return 0.0, False
    
    # Conversion factors relative to meters (1 km = 1000 m, 1 m = 1 m, etc.)
    conversion_factors = {
        'km': 1000,
        'm': 1,
        'cm': 0.01,
        'mm': 0.001
    }
    
    # Convert input to meters first
    distance_in_meters = distance * conversion_factors[unit_in]
    
    try:
        result = distance_in_meters / conversion_factors[unit_out]
        return result, True
    except ZeroDivisionError:
        return 0.0, False

def main():
    # Define argument parser without requiring mandatory arguments for the specific task logic flow
    parser = argparse.ArgumentParser(description="Convert distances between metric units.")
    
    distance_group = parser.add_mutually_exclusive_group(required=False)
    distance_group.add_argument('-d', '--distance', type=float, help='Distance value')
    unit_in_group = parser.add_mutually_exclusive_group()
    unit_in_group.add_argument('--from-unit', '-f', choices=['km', 'm', 'cm', 'mm'], default=None)
    unit_out_group = parser.add_mutually_exclusive_group()
    unit_out_group.add_argument('--to-unit', '-t', choices=['km', 'm', 'cm', 'mm'], dest='unit_to_unit', default=None)

    # Since the task requires sample values to run without user input, we will not use --help or interactive prompts.
    args = parser.parse_args()
    
    distance_value = 10.5 if args.distance is None else args.distance

if __name__ == '__main__':
    pass
