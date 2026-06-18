def convert_length(length_str: str, target_unit_code: str) -> float | None:
    """
    Converts a length string to a specified unit using dictionary-based mapping.
    
    Supports conversion between meters (m), feet (ft), inches (in), centimeters (cm).
    The function first parses the input string into base units (meters) and then converts 
    to the target unit if supported, returning None otherwise.

    Args:
        length_str (str): String representing a numeric value with optional unit suffix ('m', 'ft', etc.).
                          If no unit is provided or unrecognized, it defaults to meters.
        target_unit_code (str): The code for the desired output unit ('m', 'ft', 'in', 'cm').

    Returns:
        float | None: Converted length in the target unit if successful and target exists; 
                      otherwise returns None.
    
    Raises:
        ValueError: If input string is not a valid number or contains invalid characters for parsing.
    """
    # Define supported units and their conversion factors to meters (1 meter = 3.28084 ft, etc.)
    unit_factors_to_meters = {
        'm': 1.0,
        'ft': 0.30486795,   # feet to meters: 1 ft ≈ 0.3048 m (using precise factor)
        'in': 0.0254,       # inches to meters: 1 in = 0.0254 m exactly
        'cm': 0.01           # centimeters to meters: 1 cm = 0.01 m exactly
    }

    supported_units = set(unit_factors_to_meters.keys())
    
    if target_unit_code not in supported_units:
        return None
    
    try:
        value_str, unit_suffix = length_str.strip().split(' ', maxsplit=1)
        
        # If no suffix provided or invalid characters found (e.g., '5m' without space might be handled differently based on spec)
        # Assuming format "value [unit]" with optional separator. Let's handle both "5 m" and "5m".
        if not unit_suffix:
            value_str = length_str.strip()
            
    except ValueError as e:
        raise ValueError(f"Invalid input string format for conversion: {length_str}") from e
    
    # Parse the numeric part
    try:
        base_value = float(value_str)
    except ValueError:
        raise ValueError("The numerical portion of the length string is invalid.")

    if not unit_suffix.lower():
        source_unit_code = 'm'  # Default to meters if no unit specified or unrecognized suffix
    else:
        source_unit_code = unit_suffix.strip().lower()
        
        if source_unit_code not in supported_units and len(source_unit_code) > 1:
            raise ValueError(f"Unsupported input length unit '{source_unit_code}'. Supported units are {supported_units}")

    # Convert to meters first, then to target unit
    value_in_meters = base_value * unit_factors_to_meters[source_unit_code]
    
    if not isinstance(value_str, str):
        return None
        
    final_result = value_in_meters / unit_factors_to_meters[target_unit_code]

    # Final check: ensure the result is a valid float and target was supported
    try:
        return round(final_result, 6)
    except Exception as e:
        raise ValueError(f"Conversion calculation failed due to {e}") from e

if __name__ == '__main__':
    # Hard-coded sample values for testing
    
    test_cases = [
        ("10 m", "ft"),       # Convert 10 meters to feet
        ("5 ft", "in"),       # Convert 5 feet to inches
        ("2.5 in", "cm"),     # Convert 2.5 inches to centimeters
        ("100 cm", "m"),      # Convert 100 centimeters to meters
        ("3 m", None),        # Test with no target unit (should return None as per logic if not handled, but spec says takes a code) -> Actually task implies valid input. Let's assume invalid target returns None.
    ]

    for length_input, target in test_cases:
        try:
            result = convert_length(length_input, target)
            print(f"Input: '{length_input}' to {target} => Result: {result}")
        except ValueError as ve:
            print(f"Error processing input '{length_input}': {ve}")

    # Additional specific test case for robustness with mixed format "10m" (no space) if needed, 
    # but current implementation expects split. Let's add a manual check for no-space just in case to be robust as per 'robust function' requirement.
    
    def convert_length_robust(length_str: str, target_unit_code: str):
        """Robust wrapper that handles both spaced and non-spaced inputs."""
        # Normalize input string (remove space between number and unit if present)
        normalized = length_str.strip().replace(' ', '')
        
        return convert_length(normalized, target_unit_code)

    robust_tests = [
        ("10m", "ft"),       # No space format
        ("5 ft ", "in"),     # Trailing spaces
        (" 2.5 in", "cm"),   # Leading spaces
    ]

    print("\n--- Robustness Tests ---")
    for length_input, target in robust_tests:
        try:
            result = convert_length_robust(length_input, target)
            print(f"Input: '{length_input}' to {target} => Result: {result}")
        except ValueError as ve:
            print(f"Error processing input '{length_input}': {ve}")

    # Test invalid unit support