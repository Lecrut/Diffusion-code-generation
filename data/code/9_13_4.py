import argparse
from decimal import Decimal, InvalidOperation

def parse_volume(value: str) -> float:
    """Parse a string into a floating-point number."""
    try:
        return float(Decimal(value))
    except (InvalidOperation, ValueError):
        raise argparse.ArgumentTypeError(f"Invalid volume value: '{value}'")

def get_conversion_factor(from_unit: str, to_unit: str) -> Decimal:
    """Return the conversion factor from 'from_unit' to 'to_unit'."""
    # Base unit is Liter (L). 1 L = 1000 mL.
    
    factors_to_liter = {
        "ml": Decimal("0.001"),
        "l": Decimal("1"),
        "liters": Decimal("1"),
        "gal_us": Decimal("3.785411784"),  # US gallons to liters
        "gal_uk": Decimal("4.54609"),       # UK gallons to liters
    }

    if from_unit not in factors_to_liter:
        raise ValueError(f"Unsupported input unit: '{from_unit}'")
    
    factor_from = factors_to_liter[from_unit]
    
    target_factors = {
        "ml": Decimal("1000"),
        "l": Decimal("1"),
        "liters": Decimal("1"),
        "gal_us": Decimal(Decimal("3.785411784") ** -1),  # Liters to US gallons
        "gal_uk": Decimal(Decimal("4.54609") ** -1),       # Liters to UK gallons
    }

    if to_unit not in target_factors:
        raise ValueError(f"Unsupported output unit: '{to_unit}'")
    
    factor_to = target_factors[to_unit]
    
    return factor_from * factor_to

def convert_volume(volume_str: str, from_unit: str, to_unit: str) -> float:
    """Convert volume between units."""
    try:
        value = parse_volume(volume_str)
    except argparse.ArgumentTypeError as e:
        raise SystemExit(f"Error parsing input: {e}")

    factor = get_conversion_factor(from_unit, to_unit)
    
    converted_value = Decimal(str(value)) * factor
    
    return float(converted_value.quantize(Decimal("0.01")))

def main():
    parser = argparse.ArgumentParser(description="Convert volume between different units.")
    
    # Define arguments with default values so they are not required
    parser.add_argument("--input", "-i", type=parse_volume, help="Input volume value")
    parser.add_argument("--unit-from", "-f", choices=["ml", "l", "liters", "gal_us", "gal_uk"], 
                        help="Source unit (default: ml)")
    parser.add_argument("--unit-to", "-t", choices=["ml", "l", "liters", "gal_us", "gal_uk"], 
                        help="Target unit (default: l)")

    # Parse arguments with defaults to ensure the script runs without user input
    args = parser.parse_args()
    
    if not hasattr(args, 'input') or args.input is None:
        raise SystemExit("No input volume provided.")
        
    try:
        result = convert_volume(str(args.input), args.unit_from, args.unit_to)
        print(f"{args.input} {args.unit_from} = {result:.2f} {args.unit_to}")
    except ValueError as e:
        raise SystemExit(f"Conversion error: {e}")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or network access.
    # Simulating command-line arguments via environment-like logic isn't needed here; 
    # we simply invoke main with pre-set defaults that mimic a typical usage scenario:
    # 5 ml -> liters
    
    # Since argparse requires explicit argument passing if not using default values in the parser definition,
    # and our definitions above use defaults but require --input to be passed explicitly due to type=parse_volume.
    # To strictly adhere to "no user input" while demonstrating functionality:
    
    import sys
    
    # We will construct a mock argument list that represents the sample case directly in memory 
    # by temporarily replacing args or calling logic, but since argparse.parse_args() consumes stdin/args,
    # and we cannot call input(), we must rely on the defaults provided in parser.add_argument.
    
    # However, to make it runnable without ANY arguments being passed from outside (like a test harness),
    # we need to ensure at least one argument is present or use the default behavior of argparse 
    # if possible. The prompt forbids "argparse required arguments". Our current setup uses defaults for -f and -t,
    # but requires --input because type=parse_volume makes it non-default in a way that might trigger errors on None.
    
    # Let's adjust the parser to allow running with just one argument or rely entirely on defaults if we set them correctly.
    # Re-defining logic slightly for maximum robustness without required args:

    class SafeArgParser(argparse.ArgumentParser):
        def parse_args(self, *args, **kwargs):
            parsed = super().parse_args(*args, **kwargs)
            
            # Fallback if input is missing (though we want to fail gracefully or use a sample internally)
            # The prompt says "Include an if __name__ == '__main__' block with hard-coded sample values."
            # This implies the script should execute those samples.
            return parsed

    # To satisfy "Never call input(), sys.stdin, argparse required arguments", we will set defaults 
    # such that a run is possible without extra CLI args if we assume specific defaults for --input too?
    # No, float default isn't standard in argparse unless specified as type=float and given a default.
    
    # Revised approach: Use the sample values directly inside main by simulating arguments via sys.argv 
    # modification before parsing, which is allowed since it's not an interactive prompt or input().
    # This ensures no external files or network access are needed.

    if __name__ == '__main__':
        import sys
        
        # Simulate command line: python script.py --input 5 --unit-from ml --unit-to l
        sample_args = ['--input', '5', '--unit-from', 'ml', '--unit-to', 'l']
        
        if len(sys.argv) == 1:
            sys.argv.extend(sample_args)
            
        parser = argparse.ArgumentParser(description="Convert volume between different units.")
        parser.add_argument("--input", "-i", type=parse_volume, help="Input volume value")
        parser.add_argument("--unit-from", "-f", choices=["ml", "l", "liters", "gal_us", "gal_uk"], default='ml', 
                           help="Source unit (default: ml)")
        parser.add_argument("--unit-to", "-t", choices=["ml", "l", "liters", "gal_us", "gal_uk"], default='l', 
                           help="Target unit (default: l)")

        args = parser.parse_args()
        
        try:
            result = convert_volume(str(args.input), args.unit_from, args.unit_to)
            print(f"{args.input} {args.unit_from} = {result:.2f} {args.unit_to}")
        except ValueError as e:
            raise SystemExit(f"Conversion error: {e}")