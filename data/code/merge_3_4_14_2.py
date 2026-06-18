import argparse

def convert_distance(distance: float, from_unit: str, to_unit: str) -> float:
    """Convert distance between units using a central meter base."""
    # Define conversion factors relative to meters
    unit_factors = {
        'm': 1.0,      # meters
        'km': 1000.0,  # kilometers
        'cm': 0.01,    # centimeters
        'mm': 0.001,   # millimeters
        'mi': 1609.344,  # miles (international)
        'yd': 0.9144,   # yards
        'ft': 0.3048    # feet
    }

    if from_unit not in unit_factors or to_unit not in unit_factors:
        raise ValueError(f"Invalid units provided. Supported units are: {', '.join(unit_factors.keys())}")

    distance_in_meters = distance * unit_factors[from_unit]
    converted_distance = distance_in_meters / unit_factors[to_unit]

    return converted_distance

def main():
    parser = argparse.ArgumentParser(
        description="Convert distances between various units."
    )
    
    # Using optional arguments to prevent required input prompts while allowing CLI usage if desired later.
    # The task forbids 'input()' and interactive stdin, so this setup is safe for both direct execution 
    # with args or future manual entry via command line without blocking the script flow on error immediately.
    parser.add_argument(
        '-d', '--distance', type=float, help="The distance value to convert."
    )
    
    parser.add_argument(
        '-f', '--from_unit', default='m', choices=list(unit_factors.keys()), 
        help=f"The source unit (default: m). Supported units are: {', '.join(sorted(unit_factors.keys()))}."
    )

    parser.add_argument(
        '-t', '--to_unit', default='km', choices=list(unit_factors.keys()), 
        help="The target unit for conversion. Default is km."
    )

    args = parser.parse_args()

    try:
        result = convert_distance(args.distance, args.from_unit, args.to_unit)
        
        # Format the output nicely based on magnitude to avoid excessive decimals or scientific notation where possible
        if abs(result) < 0.01 and abs(result) > 0:
            formatted_result = f"{result:.2f}"
        else:
            formatted_result = str(round(result, 6))

        print(f"Converted {args.distance} {args.from_unit}s to {formatted_result} {args.to_unit}s")
    except ValueError as e:
        # This catches the error raised by convert_distance for invalid units or bad input types if passed incorrectly externally.
        # Since we are not using sys.stdin, this handles logic errors gracefully.
        print(f"Error: {e}", file=__import__('sys').stderr)

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements to ensure the block runs without user input or network access.
    import sys
    
    # Simulate command-line arguments for demonstration purposes within this module execution context.
    # We construct a mock argument namespace directly since we cannot use interactive prompts or stdin/stdout blocking calls 
    # that require external interaction in a non-CLI environment, but the script is designed to work as a standard CLI tool.
    
    sample_distance = 50.0
    sample_from_unit = 'm'
    sample_to_unit = 'km'

    # Create an argument object manually with our sample values for this specific execution block
    class MockArgs:
        def __init__(self, d, f, t):
            self.distance = d
            self.from_unit = f
            self.to_unit = t
    
    mock_args = MockArgs(sample_distance, sample_from_unit, sample_to_unit)

    # Override the parsed args for this specific run to match the hard-coded samples
    original_parser = None  # We won't re-parse here as it's not needed if we have our own object structure logic in main above
    
    # To strictly follow "no input()" and ensure the script runs without needing actual CLI flags passed by a shell,
    # we will execute the conversion logic directly using the hard-coded values inside this block.
    
    try:
        result = convert_distance(sample_distance, sample_from_unit, sample_to_unit)
        
        if abs(result) < 0.01 and abs(result) > 0:
            formatted_result = f"{result:.2f}"
        else:
            formatted_result = str(round(result, 6))

        print(f"Converted {sample_distance} {sample_from_unit}s to {formatted_result} {sample_to_unit}s")
    except ValueError as e:
        import sys
        # If an error occurs during the hard-coded conversion (e.g., invalid unit), log it.
        if 'Invalid units' in str(e):
            print(f"Error with sample data: Invalid units provided.", file=sys.stderr)