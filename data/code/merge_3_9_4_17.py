import argparse

def get_unit_mapping():
    """Returns a dictionary mapping unit names to their conversion factors relative to base units."""
    return {
        "kilogram": 1,
        "gram": 0.001,
        "milligram": 0.000001,
        "tonne": 1000,
        "meter": 1,
        "centimeter": 0.01,
        "kilometer": 1000,
        "mile": 1609.344,
        "yard": 0.9144,
        "foot": 0.3048,
        "inch": 0.0254,
    }

def convert_value(value: float, from_unit: str, to_unit: str) -> tuple[float, str]:
    """Converts a value between units using the base unit system."""
    mapping = get_unit_mapping()

    if from_unit not in mapping or to_unit not in mapping:
        raise ValueError(f"Invalid unit. Available units are {list(mapping.keys())}")

    # Convert source value to base unit (e.g., kilograms, meters)
    base_value = value * mapping[from_unit]

    # Convert base value to target unit
    converted_base_value = base_value / mapping[to_unit]

    return converted_base_value, f"{to_unit}"

def parse_arguments():
    """Sets up argument parsing with non-required arguments."""
    parser = argparse.ArgumentParser(
        description="Convert values between different units of measurement."
    )
    
    # Non-interactive input: allow optional volume (default to 1) and unit flags if provided, 
    # but since we cannot use required args or stdin prompts in the final execution block logic strictly as per constraints,
    # we will default everything for the sample run while keeping CLI structure robust.
    
    parser.add_argument(
        "--volume", "-v", type=float, default=100, help="The value to convert (default: 100)"
    )
    
    parser.add_argument(
        "--from-unit", "-f", 
        choices=list(get_unit_mapping().keys()), 
        required=False, 
        default=None, 
        help="Starting unit of measurement"
    )

    parser.add_argument(
        "--to-unit", "-t", 
        choices=list(get_unit_mapping().keys()), 
        required=False, 
        default=None, 
        help="Target unit for conversion"
    )
    
    return parser.parse_args()

def main():
    """Main entry point executing the CLI logic."""
    args = parse_arguments()

    # Fallback defaults if units were not explicitly provided via command line flags to ensure robustness without prompts
    from_unit = getattr(args, 'from_unit', None) or "kilogram"
    to_unit = getattr(args, 'to_unit', None) or "gram"
    
    try:
        result_value, target_str = convert_value(
            args.volume, 
            from_unit if from_unit else "meter", # Fallback for meter as base length example
            to_unit if to_unit else "kilometer"   # Fallback for kilometer as base length example
        )

        print(f"{args.volume} {from_unit or 'meter'} = {result_value:.6f} {to_unit or 'kilometer'}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the block runs without user input, network access, or pre-existing files.
    main()