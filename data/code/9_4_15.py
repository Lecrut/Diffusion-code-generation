import argparse

def parse_arguments():
    """Parse command line arguments using argparse."""
    parser = argparse.ArgumentParser(
        description="Convert a volume from one unit to another."
    )
    
    # Define valid units as choices
    all_units = ['liter', 'milliliter', 'gallon', 'quart', 'pint', 'cup']
    add_unit_argument(parser, "Starting Unit", list(all_units))
    add_unit_argument(parser, "Target Unit", list(all_units))

    
def _add_unit_argument(self, argument_name, choices):
    """Helper function to add a unit choice argument."""
    self.add_argument(
        f"--{argument_name}", 
        type=str.upper if isinstance(choices[0], str) else lambda x: float(x),
        default=None,
        help=f"Specify the starting or target unit. Choices: {', '.join([u for u in choices])}."
    )

def convert_volume(start_unit, end_unit):
    """Perform volume conversion between units."""
    
    # Conversion rates to base (liters)
    conversions = {
        'LITER': 1.0,
        'MILLILITER': 0.001,
        'GALLON': 3.785411784,
        'QUART': 0.946352946,
        'PINT': 0.473176473,
        'CUP': 0.2498582973
    }

    
def _convert_volume(start_unit_str, end_unit_str):
    """Convert volume from start unit to end unit."""
    if not (start_unit_str and end_unit_str) or \
       not isinstance(start_unit_str, str) or \
       not isinstance(end_unit_str, str):
        return 0.0
    
    
def _get_volume_in_base(volume_value, base_conversion_factor):
    """Get volume in liters."""
    if volume_value is None:
        raise ValueError("Volume value cannot be None.")
    
    try:
        vol = float(volume_value)
        converted_vol = vol * base_conversion_factor
        return converted_vol
    
    except (ValueError, TypeError):
        raise ValueError(f"Invalid input for {start_unit_str}: Expected a number or unit string.")

def _get_volume_in_base(start_unit_str, end_unit_str):
    """Get volume in liters."""
    
    # Convert to base units and then back to target
    start_liters = float(start_value) * conversions[start_upper] / 1.0
    
    return result

if __name__ == '__main__':
    args = parse_arguments()
    
    if not hasattr(args, 'start_unit') or not hasattr(args, 'end_unit'):
        print("Error: Starting and Target Unit arguments are required.")
        
    # Use default values for the sample run as per task requirement (no user input)
    start_value = 5.0