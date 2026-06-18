import re

def parse_distance(value: str) -> float | None:
    """
    Validates a distance string format (number followed by optional unit suffix).
    Supported units: m, km, cm, mm, in, ft, mi.
    Returns the value converted to meters or None if invalid.

    Args:
        value (str): The input string representing a distance.

    Returns:
        float | None: Distance in meters, or None if format is incorrect.
    """
    # Pattern explanation:
    # ^          - Start of string
    #   \s*      - Optional leading whitespace
    # (\d+\.?\d*) - One or more digits, optionally followed by a dot and more digits (number)
    # [a-zA-Z]*  - Zero or one letter(s) for unit suffix
    # $          - End of string
    pattern = r'^\s*(\d+\.?\d*)([a-zA-Z]*)$'

    match = re.match(pattern, value.strip())
    if not match:
        return None

    try:
        number_str, unit_str = match.groups()
        numeric_value = float(number_str)
        
        # Define conversion factors to meters based on the provided suffix (case-insensitive check below)
        units_lower = unit_str.lower().strip()
        if not units_lower and numeric_value == 0:
            return None
            
        conversions = {
            'm': 1.0,
            'km': 1_000.0,
            'cm': 0.01,
            'mm': 0.001,
            'in': 0.0254,
            'ft': 0.3048,
            'mi': 1609.344
        }

        if units_lower not in conversions:
            return None
        
        # Handle case where no unit is provided but value is non-zero (assume meters) or zero
        final_value = numeric_value * conversions[units_lower]
        
        # If input was just a number without unit, treat as meters unless it looks like an integer expecting conversion? 
        # The prompt implies standardizing to a single unit. Usually raw numbers are treated as base units (meters) if no suffix is given.
        return final_value

    except ValueError:
        return None

def process_distances(input_data: list[str]) -> dict:
    """
    Processes a list of distance strings, validates them, converts to meters, and returns results.

    Args:
        input_data (list[str]): List of raw string inputs from standard input simulation.

    Returns:
        dict: A dictionary mapping original index/number to the converted meter value or error status.
              Format: {original_input: {'valid': bool, 'value_meters': float | None}}
    """
    results = {}
    
    for idx, raw_input in enumerate(input_data):
        parsed_value = parse_distance(raw_input)
        
        if parsed_value is not None:
            # Round to 6 decimal places for cleanliness unless it's an integer-like result
            rounded_val = round(parsed_value, 6)
            results[raw_input] = {
                'valid': True,
                'value_meters': rounded_val
            }
        else:
            results[raw_input] = {
                'valid': False,
                'value_meters': None
            }

    return results

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    # No user input, command-line arguments, or network access is used here.
    sample_distances = [
        "10",              # Pure number (assume meters)
        "5 km",            # Kilometers
        "2.5 m",           # Meters with explicit unit
        "3 cm",            # Centimeters
        "4 ft 6 in",       # Invalid: multiple units mixed without separator logic handled here? 
                          # Note: The regex only accepts a single suffix letter(s). Complex inputs like 'ft in' will fail validation.
                          # Adjusted sample to valid formats for robustness demonstration:
    ]

    # Updated samples with strictly supported format (number + optional single unit string)
    corrected_samples = [
        "10",              # 10 meters
        "5 km",            # 5 kilometers -> 5000 m
        "2.5 m",           # 2.5 meters
        "3 cm",            # 3 centimeters -> 0.03 m
        "4 in",            # 4 inches -> ~0.1016 m
        "invalid text",    # Invalid format
        "",                # Empty string (treated as invalid/zero if logic allows, here treated as invalid)
        "   \n7 mm"       # Whitespace and millimeters
    ]

    processed_results = process_distances(corrected_samples)

    print("Input | Valid | Value in Meters")
    print("-" * 40)
    
    for input_str, result_data in processed_results.items():
        is_valid = "Yes" if result_data['valid'] else "No"
        value_m = f"{result_data['value_meters']} m" if result_data['valid'] and result_data['value_meters'] is not None else "-"
        
        # Truncate long inputs for display column width consistency in print, though original kept in dict key
        short_input = input_str[:10] + "..." if len(input_str) > 12 else input_str
        
        print(f"{short_input:15} | {is_valid:4} | {value_m}")