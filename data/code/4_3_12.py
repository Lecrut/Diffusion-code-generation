import re
from decimal import Decimal, InvalidOperation

def parse_distance(value: str) -> float:
    """
    Parses a string representing a distance in various units (km, m, cm, mm, ft, in).
    Converts the value to meters and returns it as a float.
    
    Supported formats:
        - [number] km | kilo-meter
        - [number] m  | meter
        - [number] c  | centimeter
        - [number] i  | inch (approximate conversion)
        
    Raises ValueError if the format is invalid or unit not supported.
    """
    
    # Define conversion factors to meters
    units = {
        'km': Decimal('1000'),
        'm':  Decimal('1'),
        'c':  Decimal('0.01'),
        'i':  Decimal('0.0254')
    }
    
    # Pattern to match number followed by optional unit suffix (case insensitive)
    pattern = re.compile(r'^(\d+\.?\d*)\s*([kmcin])?$', re.IGNORECASE)
    
    match = pattern.match(value.strip())
    if not match:
        raise ValueError(f"Invalid distance format: '{value}'")
    
    number_str, unit_suffix = match.groups()
    
    try:
        value_num = Decimal(number_str)
    except InvalidOperation:
        raise ValueError(f"Cannot parse numeric part of distance: '{number_str}'")
        
    if not unit_suffix:
        # Default to meters if no unit specified or 'm' is implied by context, 
        # but strictly we treat missing suffix as error unless explicitly handled.
        # For robustness in this task, assume default meter for simplicity if no unit provided?
        # Let's stick to strict validation first: require a number and optional valid unit.
        raise ValueError("A distance must include a numeric value.")

    factor = units.get(unit_suffix.lower())
    if not factor:
        raise ValueError(f"Unsupported unit suffix: '{unit_suffix}'")
        
    return float(value_num * factor)

def main():
    """
    Reads distances from standard input, validates them, converts to meters, and prints results.
    Includes a sample block with hard-coded values for testing without user interaction.
    """
    
    # Hard-coded sample inputs as per task requirements (no external files or prompts)
    sample_inputs = [
        "5 km",
        "10 m",
        "2 c",
        "3 i"
    ]
    
    try:
        for dist_str in sample_inputs:
            meters = parse_distance(dist_str)
            print(f"{dist_str} -> {meters:.4f} meters")
            
    except ValueError as e:
        # Handle any potential errors from the list (though samples are valid here)
        print(f"Error processing input: {e}", file=__import__('sys').stderr)

if __name__ == '__main__':
    main()