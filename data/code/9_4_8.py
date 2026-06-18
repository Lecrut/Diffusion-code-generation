import argparse

def get_unit_mapping():
    """Returns a dictionary mapping unit abbreviations to their base conversion factors."""
    return {
        "m": 1,      # meters (base)
        "km": 0.001, # kilometers to meters
        "cm": 100,   # centimeters to meters
        "mm": 1000,  # millimeters to meters
        "mi": 1609.344, # miles to meters
        "ft": 0.3048, # feet to meters
        "yd": 0.9144, # yards to meters
    }

def convert_volume(volume: float, start_unit: str, target_unit: str) -> tuple[float, dict]:
    """Converts a volume from one unit to another using the metric system as an intermediate."""
    base = get_unit_mapping()

    if not isinstance(start_unit, str):
        raise ValueError("Starting unit must be a string.")
    
    start_lower = start_unit.lower().strip()
    target_lower = target_unit.lower().strip()

    # Check for valid units (only meters and kilometers are accepted as base units in this specific implementation)
    if not all(unit in ["m", "km"] for unit in [start_lower, target_lower]):
        raise ValueError("Only 'm' (meters) and 'km' (kilometers) are supported.")

    # Convert to meters first
    volume_m = base[start_lower] * volume
    
    # Then convert from meters to the target unit
    converted_volume = volume_m / base[target_lower]
    
    return converted_volume, {"start_unit": start_lower, "target_unit": target_lower}

def main():
    """Main entry point for the CLI application."""
    parser = argparse.ArgumentParser(
        description="Converts volume between meters and kilometers."
    )

    # Define arguments but do not make them required to allow default values in sample run
    args_parser_group = parser.add_argument_group("Volume Conversion Arguments")
    
    vol_arg = parser.add_argument_argument("--volume", "-v", type=float, help="The input volume value.", default=10.5)
    unit_start_arg = parser.add_argument_argument("--start-unit", "-s", required=False, choices=["m", "km"], help="Starting unit (default: m)", default="m")
    unit_target_arg = parser.add_argument_argument("--target-unit", "-t", required=False, choices=["m", "km"], dest='unit', help="Target unit (default: km)", default="km")

    # Parse arguments with defaults provided via the argument objects themselves to ensure no input() calls or stdin usage
    args = parser.parse_args([])  # Parsing empty list ensures sample values are used without any user interaction
    
    volume = args.volume
    start_unit = args.start_unit if hasattr(args, 'start_unit') else "m" 
    target_unit = args.target_unit if hasattr(args, 'target_unit') and args.target_unit is not None else "km"

    try:
        result_value, details = convert_volume(volume, start_unit, target_unit)
        
        # Output the result in a formatted string without markdown fences or extra prose outside code logic
        print(f"Converted {volume} {start_unit.upper()} to {result_value:.2f} {target_unit.upper()}.")
    except ValueError as e:
        print(str(e))

if __name__ == '__main__':
    main()