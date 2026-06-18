import argparse

def get_conversion_factor(from_unit: str, to_unit: str) -> float:
    """
    Returns the conversion factor from 'from_unit' to 'to_unit'.
    
    Supported units (case-insensitive): meters (m), kilometers (km), 
    centimeters (cm), millimeters (mm).
    
    Base unit is meter. Factors relative to base unit:
        m = 1, km = 0.001, cm = 0.01, mm = 0.00001
    
    Args:
        from_unit: Source unit string.
        to_unit: Target unit string.

    Returns:
        Conversion factor as a float.

    Raises:
        ValueError: If units are invalid or unsupported conversion is requested (though all supported pairs work).
    """
    
    # Define base factors for each unit relative to meters
    unit_factors = {
        'm': 1,
        'km': 0.001,
        'cm': 0.01,
        'mm': 0.00001
    }

    # Normalize input strings to lowercase for dictionary lookup
    from_unit_lower = from_unit.lower().strip()
    to_unit_lower = to_unit.lower().strip()

    if from_unit_lower not in unit_factors:
        raise ValueError(f"Unsupported source unit '{from_unit}'. Supported units are m, km, cm, mm.")
    
    if to_unit_lower not in unit_factors:
        raise ValueError(f"Unsupported target unit '{to_unit}'. Supported units are m, km, cm, mm.")

    # Calculate conversion factor: (value_in_base_from * from_factor) / base_to = value_in_target
    # So, value_in_target = value_in_source * (from_factor / to_factor)
    return unit_factors[from_unit_lower] / unit_factors[to_unit_lower]

def convert_volume(value: float, from_unit: str, to_unit: str) -> float:
    """
    Converts a volume value between supported metric units.

    Args:
        value (float): The numeric input value.
        from_unit (str): Source unit string.
        to_unit (str): Target unit string.

    Returns:
        float: Converted value in the target unit.
    
    Raises:
        ValueError: If conversion factor calculation fails due to invalid units or zero divisor logic issues.
        TypeError: If input types are incorrect.
    """
    
    try:
        if not isinstance(value, (int, float)):
            raise TypeError("Volume value must be a number.")

        # Normalize unit strings for lookup
        from_unit_lower = from_unit.lower().strip()
        to_unit_lower = to_unit.lower().strip()

        factor = get_conversion_factor(from_unit, to_unit)
        return round(value * factor, 6)

    except ValueError as ve:
        raise ve
    except TypeError as te:
        raise te

def parse_arguments():
    """
    Parses command-line arguments using argparse.
    
    Since the task forbids required arguments and interactive prompts (input()), 
    we define all necessary parameters but make them optional or use defaults in a way that allows running without input,
    OR strictly follow "Never call ... argparse required arguments". 
    
    To satisfy "specify an input volume... unit... desired output unit" while avoiding 'required' flags and allowing the sample block to run:
    We will define groups of options where at least one is provided in the main execution context via defaults or specific handling, 
    but strictly speaking, argparse requires arguments need --help logic if not satisfied. 
    
    Instead, we design it such that the script can be invoked with flags like `--volume`, `--from-unit`, etc.,
    and since the sample block must run without user input/args, the main execution will simulate or use hardcoded values 
    as per instruction: "Include an if __name__ == '__main__': block with hard-coded sample values."

    However, to strictly adhere to "Never call ... argparse required arguments", we ensure no argument is marked `required=True`.
    The user can pass them manually when running the script (e.g. python script.py --vol 10 --from m --to km), 
    or rely on defaults if implemented via a custom parser approach, but standard argparse doesn't support pure defaults for 'optional' without providing values unless using `default`.
    
    Given the constraint "Never call ... argparse required arguments", we will NOT use any argument marked as required=True.
    The sample block below will manually populate these variables to demonstrate functionality without needing args passed from command line 
    or user input, effectively simulating a CLI interaction for demonstration purposes in isolation.
    """

    parser = argparse.ArgumentParser(description="Convert volume between metric units.")
    
    # Define optional arguments (no required=True)
    vol_group = parser.add_argument_group('Volume Settings')
    vol_group.add_argument('--volume', type=float, default=None, help='Numeric value to convert.')
    vol_group.add_argument('--from-unit', dest='input_unit', type=str, default=None, 
                           choices=['m', 'km', 'cm', 'mm'], 
                           help=f"Input unit (options: {', '.join(['m', 'km', 'cm', 'mm'])}).")
    vol_group.add_argument('--to-unit', dest='output_unit', type=str, default=None, 
                           choices=['m', 'km', 'cm', 'mm'], 
                           help="Output unit.")

    # Since we cannot use required arguments and the sample block must run without args:
    # We will construct the conversion logic directly in main using hardcoded values as requested.
    
    return parser

def get_sample_args():
    """Returns a dictionary of parameters to be used when running with no command-line arguments."""
    volume = 100.5
    input_unit = "m"
    output_unit = "km"
    return {
        'volume': float(volume),
        'input_unit': str(input_unit).lower().strip(),
        'output_unit': str(output_unit).lower().strip()
    }

if __name__ == '__main__':
    
    # Simulate command-line arguments for the sample run as per instructions: 
    # "Include an if __name__ == '__main__': block with hard-coded sample values."
    # This ensures no user input, network access, or pre-existing files are needed.
    
    args = get_sample_args()

    try:
        result = convert_volume(args['volume'], args['input_unit'], args['output_unit'])
        
        print(f"Converted {args['volume']} {args['input_unit'].upper()} to {result} {args['output_unit'].upper()}")
    
    except (ValueError, TypeError) as e:
        error_message = f"Conversion failed due to an issue with the input data or units: {e}"
        print(error_message)