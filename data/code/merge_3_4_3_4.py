import re
from typing import List, Tuple

def parse_distance_input(distance_str: str) -> float:
    """
    Validates and parses a distance string into meters.
    
    Supports formats like '5', '10m', '2km', '3hm'.
    Raises ValueError if the format is invalid or conversion fails.
    """
    # Regex pattern to match optional number followed by an optional unit (m, km, hm)
    # Pattern: digits and decimal points allowed; units are m, km, or hm (case-insensitive for robustness though we handle lowercase primarily)
    pattern = r'^(\d+\.?\d*)([mkh])?$'
    
    match = re.match(pattern, distance_str.strip())
    if not match:
        raise ValueError(f"Invalid input format: '{distance_str}'. Expected a number with optional unit (m, km, hm).")
    
    value_part = float(match.group(1))
    unit_part = match.group(2) or 'm'  # Default to meters
    
    try:
        meter_value = value_part
        
        if unit_part == 'km':
            meter_value *= 1000.0
        elif unit_part == 'hm':
            meter_value *= 100.0
            
        return meter_value
    except ValueError as e:
        raise ValueError(f"Failed to parse numeric value in '{distance_str}': {e}")

def process_distances(input_data: List[str]) -> Tuple[List[float], str]:
    """
    Processes a list of distance strings, converting them all to meters.
    
    Args:
        input_data (List[str]): Raw string inputs from source.
        
    Returns:
        Tuple[List[float], str]: 
            - A list containing the distances in meters.
            - An error message if any conversion failed, or empty string if success.
    """
    results = []
    
    for idx, item in enumerate(input_data):
        try:
            converted_value = parse_distance_input(item)
            results.append(converted_value)
        except ValueError as e:
            # Aggregate error message indicating which input failed and why
            return [], f"Error processing distance at index {idx}: {e}"
            
    if not results:
        return [], "No valid distances found in the provided data."
        
    return results, ""

if __name__ == '__main__':
    # Hard-coded sample values to simulate input without user interaction or files.
    # These represent mixed units and potential edge cases for validation.
    SAMPLE_INPUTS = [
        "5",           # Meters (default)
        "10m",         # Explicit meters
        "2km",         # Kilometers
        "3hm",         # Hectometers
        "7.5",         # Decimal value in base unit
    ]
    
    if not SAMPLE_INPUTS:
        print("Error: No sample data provided.")
        
    results, error_msg = process_distances(SAMPLE_INPUTS)
    
    if error_msg != "":
        print(f"Conversion failed due to errors:\n{error_msg}")
    else:
        # Print the standardized values in meters separated by newlines for clarity.
        output_lines = [f"{val} m" for val in results]
        print("\n".join(output_lines))