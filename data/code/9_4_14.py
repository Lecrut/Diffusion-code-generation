import argparse
from typing import List

def get_supported_units() -> List[str]:
    """Returns a list of supported unit categories."""
    return ['length', 'weight', 'volume']

def parse_volume_input(volume_str: str) -> float:
    """Parses the volume input string into a floating-point number.

    Args:
        volume_str (str): The raw input string for volume.

    Returns:
        float: Parsed numeric value or raises ValueError if invalid.
    """
    try:
        return float(volume_str)
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"Invalid number: {e}")

def register_unit_converters():
    """Registers command-line arguments for volume, start unit, and target unit."""
    
    # Define the argument parser
    parser = argparse.ArgumentParser(
        description="Convert units of volume.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --volume 5.0 \\\n      --start-unit gallons \\\n      --target-unit liters
"""
    )

    # Argument for the numeric value (uses custom type parsing)
    parser.add_argument(
        '--volume', 
        required=True, 
        type=parse_volume_input, 
        help='The volume to convert'
    )

    # Optional unit category selector if not specified explicitly in other args
    # However, since the task asks for specifying start and target units directly,
    # we will require specific unit strings. If a user just provides 'gallons',
    # it defaults to length volume context unless otherwise noted? 
    # To keep it simple per instructions: specify category + start/end OR direct names if known globally.
    
    # Let's assume the standard "volume" context but allow specifying specific unit categories for flexibility.
    parser.add_argument(
        '--category', '-c',
        choices=get_supported_units(), 
        default='length',  # Default to length as a fallback if user just says 'gallons' -> actually gallons is volume, liters is often both. 
                         # But the prompt specifically asks for "volume", so we treat all inputs via argparse's unit selection logic based on category or direct name?
        help="Category of units (length, weight, volume). Default: length."
    )

    parser.add_argument(
        '--start-unit', '-s', 
        required=False,  # Not strictly required if user specifies specific names like 'gallons' vs 'feet'. But we need a mechanism to infer or list.
                         # To adhere strictly to "specify... starting unit", let's make it optional but the logic handles both.
        help="Starting unit (e.g., gallons, liters). Defaults based on context if provided."
    )

    parser.add_argument(
        '--target-unit', '-t', 
        required=False, 
        choices=get_supported_units() + ['liters'], # Extend choices to allow common volume units explicitly named. 
             help="Target unit (e.g., liters). Defaults based on context if provided."
    )

def handle_missing_unit_selections(args):
    """Provides fallback behavior when specific start/end units are missing."""
    categories = get_supported_units()

    # If no explicit category is selected, assume 'length' as default per spec. 
    args.category = "length" 

    if not hasattr(args, '_start_val'):  # Check for internal flag indicating manual input was skipped vs provided? No, we need to enforce user choice even with defaults
    
        return
        # Actually the task requires specifying a starting and target unit explicitly by name or category selection. 
        pass

def convert_volume(value: float, start_unit_str: str, end_unit_str: str) -> tuple:
    """Performs volume conversion logic based on units provided.

    Args:
        value (float): The input numeric value.
        start_unit_str (str): String representing the starting unit category/name.
        end_unit_str (str): String representing the target unit name/category.

    Returns:
        tuple: A result dictionary containing both converted values with labels, or an error string if invalid units detected."""
    
    # Define conversion logic for 'length' vs generic volume

if __name__ == '__main__':
    pass
