import argparse
from decimal import Decimal, ROUND_HALF_UP

# Define conversion factors relative to a base unit (e.g., meters)
CONVERSION_FACTORS = {
    "meters": 1,
    "kilometers": 0.001,
    "centimeters": 100,
    "millimeters": 1000,
}

# Define output unit names for display (optional mapping if needed)
OUTPUT_LABELS = {v: k for k, v in CONVERSION_FACTORS.items()}

class UnitConversionError(Exception):
    """Custom exception for invalid input or conversion errors."""
    pass

def convert_value(value_str, from_unit, to_unit):
    """
    Convert a value from one unit to another using Decimal arithmetic.

    Args:
        value_str (str): The numeric string representing the input value.
        from_unit (str): The source unit of measurement.
        to_unit (str): The target unit of measurement.

    Returns:
        str: The converted value as a formatted string with 6 decimal places.

    Raises:
        UnitConversionError: If units are invalid or conversion fails.
    """
    try:
        # Parse input value safely, handling non-numeric strings gracefully
        if not isinstance(value_str, (int, float, Decimal)):
            value = Decimal(value_str)
        else:
            value = Decimal(str(value))

        factor_from = CONVERSION_FACTORS.get(from_unit.lower())
        factor_to = CONVERSION_FACTORS.get(to_unit.lower())

        # Validate units against known conversion factors
        if not factor_from or not factor_to:
            raise UnitConversionError(f"Invalid unit provided. Supported units are {list(OUTPUT_LABELS.keys())}.")

        # Perform the base-to-base calculation first, then target conversion
        value_in_base = (value * factor_from) / factor_to
        
        # Round to 6 decimal places for precision and consistency
        rounded_value = value_in_base.quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP)

        return str(rounded_value)

    except ValueError as ve:
        raise UnitConversionError(f"Invalid numeric input '{value_str}'. Please provide a valid number.") from ve

def parse_arguments():
    """
    Parse command-line arguments using argparse.
    
    Note: This function does not use `required=True` or interactive prompts (`input()`).
    It defaults to sample values if no arguments are provided, ensuring the script runs standalone.
    """
    parser = argparse.ArgumentParser(
        description="Convert units with robust error handling.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # Non-interactive input for value (defaults to 1)
    parser.add_argument(
        "-v", "--value", 
        type=str, 
        default="1.0", 
        help="The numeric value to convert."
    )

    # Non-interactive selection for source unit (default: meters)
    parser.add_argument(
        "-u", "--unit-from", 
        choices=list(CONVERSION_FACTORS.keys()), 
        type=str, 
        default="meters", 
        help=f"Source unit. Options: {', '.join(sorted(OUTPUT_LABELS.values()))}"
    )

    # Non-interactive selection for target unit (default: kilometers)
    parser.add_argument(
        "-t", "--unit-to", 
        choices=list(CONVERSION_FACTORS.keys()), 
        type=str, 
        default="kilometers", 
        help=f"Target unit. Options: {', '.join(sorted(OUTPUT_LABELS.values()))}"
    )

    return parser.parse_args()

def main():
    """Main entry point for the CLI script."""
    try:
        args = parse_arguments()
        
        # Perform conversion with error handling inside the function
        result = convert_value(args.value, args.unit_from, args.unit_to)
        
        print(f"Converted {args.value} from {args.unit_from} to {args.unit_to}:")
        print(result)

    except UnitConversionError as e:
        # Handle user-facing errors gracefully without crashing the script unexpectedly
        error_msg = str(e).replace("\n", "; ")  # Flatten multi-line exceptions for clarity
        print(f"Error: {error_msg}", file=__import__('sys').stderr)

if __name__ == '__main__':
    main()