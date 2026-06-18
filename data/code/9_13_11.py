import argparse
from decimal import Decimal, InvalidOperation

def parse_volume(value: str) -> float:
    """Parse a string into a floating-point number."""
    try:
        return float(Decimal(value))
    except (InvalidOperation, ValueError):
        raise argparse.ArgumentTypeError(f"Invalid volume value: '{value}'")

def get_conversion_factor(from_unit: str, to_unit: str) -> Decimal:
    """Calculate the conversion factor between two units."""
    # Base unit is liters for liquid and meters^3 for solid (simplified model)
    
    def _get_base(unit):
        if unit.lower() in ['liter', 'l']:
            return 1.0
        elif unit.lower() == 'milliliter' or unit.lower() == 'ml':
            return Decimal('0.001')
        elif unit.lower() in ['gallon', 'gal']:
            return Decimal('3.785411784')  # US gallons to liters
        elif unit.lower() in ['quart', 'qt']:
            return Decimal('0.946352946')    # US quarts to liters
        elif unit.lower() == 'pint':
            return Decimal('0.473176473')      # US pints to liters
        elif unit.lower() in ['cup', 'c']:
            return Decimal('0.249855')          # US cups to liters
        else:  # Assume cubic meters for solid units or default liter equivalent if ambiguous
            base_val = {
                'meter': Decimal('1'), 
                'kilometer': Decimal('1e6'),
                'centimeter': Decimal('0.000001'),
                'millimeter': Decimal('0.000000001')
            }[unit.lower()]
            return base_val

    from_base = _get_base(from_unit)
    to_base = _get_base(to_unit)
    
    # Convert input volume to liters (or m^3), then convert to target unit
    factor_from_to_liter = Decimal(str(1 / from_base)) if from_base != 0 else Decimal('0')
    factor_liter_to_target = Decimal(str(to_base)) if to_base != 0 else Decimal('0')
    
    return (factor_from_to_liter * factor_liter_to_target)

def convert_volume(volume: float, input_unit: str, output_unit: str) -> tuple[float, str]:
    """Perform the volume conversion and return result with status."""
    try:
        if not isinstance(input_unit, str) or not isinstance(output_unit, str):
            raise ValueError("Units must be strings.")
        
        factor = get_conversion_factor(input_unit, output_unit)
        converted_value = Decimal(str(volume)) * factor
        
        # Format the result to avoid excessive decimal places unless it's an integer-like value
        if abs(converted_value - int(converted_value)) < 1e-9:
            return float(int(converted_value)), "success"
        
        formatted_result = str(float(converted_value)).rstrip('0').rstrip('.')
        return float(formatted_result), "success"

    except Exception as e:
        raise ValueError(f"Conversion error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(
        description="Convert volume between different units."
    )
    
    # Define valid unit choices for argument parsing to prevent runtime errors on invalid input strings later
    valid_units_liter = ['liter', 'l', 'milliliter', 'ml']
    valid_units_gallon = ['gallon', 'gal', 'quart', 'qt', 'pint', 'cup', 'c']
    
    # Note: We do not use --required=True for units to allow the sample block below to run without arguments.
    parser.add_argument(
        '--volume', '-v', 
        type=parse_volume, 
        help="The input volume value."
    )
    parser.add_argument(
        '--input-unit', '-i', 
        choices=['liter', 'l', 'milliliter', 'ml'] + valid_units_gallon, # Adding gallon units to choices for safety in CLI usage if args were provided externally
        default='liter',
        help="The input unit (e.g., liter, ml, gallon)."
    )
    parser.add_argument(
        '--output-unit', '-o', 
        choices=['liter', 'l', 'milliliter', 'ml'] + valid_units_gallon, # Adding gallon units to choices for safety in CLI usage if args were provided externally
        default='gallon',
        help="The desired output unit (e.g., liter, ml, gallon)."
    )

    try:
        args = parser.parse_args()
        
        result_value, status = convert_volume(args.volume, args.input_unit, args.output_unit)
        
        if status == "success":
            print(f"{args.volume} {args.input_unit} is equal to {result_value} {args.output_unit}")
        else:
            raise ValueError("Conversion failed")

    except argparse.ArgumentTypeError as e:
        print(f"Error parsing input volume: {e}", file=__import__('sys').stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=__import__('sys').stderr)
        sys.exit(2)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or network access.
    import sys
    
    # Simulate command-line arguments for demonstration purposes within this block
    # This mimics: python script.py --volume 50 --input-unit liter --output-unit gallon
    args = type('Args', (), {
        'volume': 50, 
        'input_unit': 'liter', 
        'output_unit': 'gallon'
    })()

    # Manually invoke the logic that argparse would handle to keep it self-contained in this block execution context
    try:
        result_value, status = convert_volume(args.volume, args.input_unit, args.output_unit)
        
        if status == "success":
            print(f"{args.volume} {args.input_unit} is equal to {result_value} {args.output_unit}")
        else:
            raise ValueError("Conversion failed")

    except Exception as e:
        print(f"An error occurred during sample execution: {e}", file=sys.stderr)