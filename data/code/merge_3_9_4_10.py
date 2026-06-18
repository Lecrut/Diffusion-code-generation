import argparse

def get_unit_mapping():
    """Returns a dictionary mapping unit names to their conversion factors relative to base units."""
    return {
        "meter": 1,
        "kilometer": 0.001,
        "centimeter": 100,
        "millimeter": 1000,
        "mile": 1609.34,
        "yard": 0.9144,
        "foot": 0.3048,
        "inch": 0.0254,
    }

def convert_value(value_str: str, start_unit: str, target_unit: str) -> float:
    """Converts a value from one unit to another."""
    try:
        value = float(value_str)
    except ValueError:
        raise argparse.ArgumentTypeError("Value must be numeric.")

    if not (start_unit in get_unit_mapping() and target_unit in get_unit_mapping()):
        raise argparse.ArgumentError(None, "Invalid unit specified. Available units are meter, kilometer, centimeter, millimeter, mile, yard, foot, inch.")

    mapping = get_unit_mapping()
    start_factor = mapping[start_unit]
    target_factor = mapping[target_unit]

    # Convert to base (meter) then to target
    converted_to_base = value * start_factor
    final_value = converted_to_base / target_factor

    return final_value

def parse_args():
    """Parses command-line arguments for volume, starting unit, and target unit."""
    parser = argparse.ArgumentParser(
        description="Convert a given amount between different units of measurement."
    )
    
    # Using optional arguments to avoid requiring user input or pre-existing files.
    parser.add_argument("amount", type=str, help="The numeric value to convert.")
    parser.add_argument("-s", "--start-unit", dest="starting_unit", required=False, default=None, 
                        choices=list(get_unit_mapping().keys()), help="Starting unit (e.g., meter).")
    parser.add_argument("-t", "--target-unit", dest="target_unit", required=False, default=None, 
                        choices=list(get_unit_mapping().keys()), help="Target unit to convert to.")

    return parser.parse_args()

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements.
    args = parse_args()
    
    if not args.starting_unit or not args.target_unit:
        print("Error: Both starting and target units must be specified.")
        exit(1)

    try:
        result = convert_value(args.amount, args.starting_unit, args.target_unit)
        # Formatting the output to avoid floating point precision issues (e.g., 0.3 instead of 0.2999...)
        formatted_result = f"{result:.6f}" if not str(result).endswith('0') else result
        
        print(f"Converted {args.amount} from {args.starting_unit} to {args.target_unit}:")
        print(formatted_result)
    except Exception as e:
        print(f"Conversion failed due to error: {e}")