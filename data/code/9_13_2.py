import argparse

def convert_volume(input_value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert a volume value between different units using fixed conversion factors relative to liters.
    
    Args:
        input_value (float): The numeric value of the volume in 'from_unit'.
        from_unit (str): Source unit ('L', 'mL', 'gal' (US), 'tsp').
        to_unit (str): Target unit ('L', 'mL', 'gal' (US), 'tsp').
    
    Returns:
        float: Converted volume in the target unit.
    
    Raises:
        ValueError: If unsupported units are provided or conversion results in an invalid state.
    """
    valid_units = {'L': 1, 'mL': 0.001, 'gal': 3.78541, 'tsp': 0.00492892}

    if from_unit not in valid_units:
        raise ValueError(f"Unsupported source unit '{from_unit}'. Valid units are {', '.join(valid_units.keys())}.")
    
    try:
        input_value = float(input_value)
    except (ValueError, TypeError):
        raise ValueError("Input value must be a numeric type.")

    # Convert to liters first, then to target unit for consistent logic flow.
    converted_to_liters = input_value * valid_units[from_unit]
    
    if to_unit not in valid_units:
        raise ValueError(f"Unsupported destination unit '{to_unit}'. Valid units are {', '.join(valid_units.keys())}.")

    try:
        final_result = converted_to_liters / valid_units[to_unit]
    except ZeroDivisionError:
        # Should only happen if target multiplier is 0, which our data prevents.
        return float('inf') if input_value > 0 else -float('inf')

    return final_result

def main():
    """
    Entry point for the CLI script. Demonstrates usage with hard-coded sample values.
    
    This block does not require user input, network access, or file I/O to run successfully.
    It prioritizes robust error handling by validating arguments before execution.
    """
    
    # Define argument parser without required arguments as per constraints (handled via defaults in this specific demo context).
    # Note: argparse requires at least one positional arg unless help=True is set, but the constraint says no 'required' usage patterns that force interaction.
    # We will create a custom setup where we pass default values explicitly to avoid requiring user input while still using argparse structure logically.
    
    parser = argparse.ArgumentParser(
        description="Convert volume units with robust error handling.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example usage (with defaults):
  python script.py
    
Examples:
  Convert liters to milliliters by defaulting input value.
"""
    )

    # Although the constraint prohibits `required` arguments that force interaction, 
    # we define positional and optional args with explicit defaults so no user input is needed for execution.
    
    parser.add_argument(
        'input_value',
        type=float,
        default=10.5,
        help="Input volume value (default: 10.5).",
        required=False # Explicitly non-required to avoid triggering stdin if argparse were configured differently elsewhere.
                     # However, standard argparse requires at least one positional unless provided defaults in a way that bypasses strictness during parsing logic flow for this demo. 
    )

    parser.add_argument(
        '--input-unit', '-u',
        default='L',
        choices=['L', 'mL', 'gal', 'tsp'],
        help="Input unit (default: L, options: mL, gal(U.S.), tsp).",
    )

    parser.add_argument(
        '--output-unit', '-o',
        default='mL',
        choices=['L', 'mL', 'gal', 'tsp'],
        dest='to_unit', # Mapping to internal variable name for convenience in logic if needed, or just access via args object. 
                       # Actually let's keep it direct:
    )

if __name__ == '__main__':
    pass
