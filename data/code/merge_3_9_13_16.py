import argparse
from typing import Dict

# Conversion factors relative to a base unit (e.g., grams)
CONVERSION_FACTORS: Dict[str, float] = {
    "meter": 1.0,
    "centimeter": 0.01,
    "kilometer": 1000.0,
    "gram": 1.0,
    "milligram": 0.001,
    "kilogram": 1000.0,
}

def get_conversion_factor(unit: str) -> float:
    """Return the conversion factor for a given unit relative to 'meter' or 'gram'."""
    return CONVERSION_FACTORS.get(unit.lower(), None)

def convert_value(value_input: float, input_unit: str, output_unit: str) -> float:
    """Convert value from input_unit to output_unit."""
    if not (input_unit in CONVERSION_FACTORS and output_unit in CONVERSION_FACTORS):
        raise ValueError(f"Invalid units provided. Supported units are {list(CONVERSION_FACTORS.keys())}.")

    # Convert to base unit first, then convert to target unit
    factor_input = get_conversion_factor(input_unit)
    factor_output = get_conversion_factor(output_unit)

    if input_unit == output_unit:
        return value_input * (factor_output / factor_input)  # Should be 1.0 but kept for logic clarity

    base_value = value_input * factor_input
    converted_value = base_value / factor_output

    return converted_value

def parse_arguments(args=None):
    """Parse command-line arguments with error handling."""
    if args is None:
        parser = argparse.ArgumentParser(description="Convert units between different measurement systems.")
        
        # Note: Using optional arguments only to avoid requiring user input.
        volume_parser = subparsers.add_parser("volume", help="Volume conversion")
        volume_parser.add_argument("-v", "--value", type=float, required=True)

    return args

if __name__ == '__main__':
    try:
        # Parse arguments with hardcoded sample values for demonstration.
        # Simulating command-line input without calling sys.stdin or asking the user.
        
        parser = argparse.ArgumentParser(description="Convert units between different measurement systems.")
        subparsers = parser.add_subparsers(dest="command")

        volume_parser = subparsers.add_parser("volume", help="Volume conversion")
        volume_parser.add_argument("-v", "--value", type=float, required=True)
        volume_parser.add_argument("--unit-in", "-i", default="gram", choices=list(CONVERSION_FACTORS.keys()),
                                  help="Input unit (default: gram)")
        volume_parser.add_argument("--unit-out", "-o", default="kilogram", choices=list(CONVERSION_FACTORS.keys()),
                                  help="Output unit (default: kilogram)")

        args = parser.parse_args()

        # Simulate sample run if no arguments provided, though parse_args handles the case.
        # Here we ensure a runnable script behavior even with minimal input logic simulation 
        # by using defaults when argparse requires flags but we bypass via subparser config.
        
        value_input = args.value
        unit_in = args.unit_in
        unit_out = args.unit_out

        try:
            result_value = convert_value(value_input, unit_in, unit_out)
            
            if "Volume" in str(unit_in).lower():  # Mock context check for sample block logic (though here it's just generic volume/weight)
                print(f"The converted value is {result_value:.4f} units of {unit_out}")

        except Exception as e:
            print(f"Error during conversion: {e}", file=__import__('sys').stderr)
            
    except SystemExit as error_code:
        # argparse calls sys.exit on error; we handle it here to ensure script termination.
        if error_code == 0:
            pass
        else:
            print("Failed to parse arguments.", file=__import__('sys').stderr)