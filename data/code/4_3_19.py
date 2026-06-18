import re
from typing import List, Tuple

def parse_distance_input(distance_str: str) -> float:
    """
    Parses a distance string into meters.
    
    Supports formats like '10', '5m', '2km', '300cm'.
    Raises ValueError if the format is invalid or conversion fails.
    """
    pattern = r'^(\d+(?:\.\d+)?)\s*([a-zA-Z]+)?$'
    
    match = re.match(pattern, distance_str.strip())
    if not match:
        raise ValueError(f"Invalid input format: '{distance_str}'")

    value_str, unit_str = match.groups()
    
    # Define conversion factors to meters
    units_map = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.344,
    }

    if not unit_str:
        # Assume meters if no unit is provided
        return float(value_str) * units_map['m']

    unit_lower = unit_str.lower()
    
    if unit_lower not in units_map:
        raise ValueError(f"Unsupported distance unit: '{unit_str}'")

    try:
        value = float(value_str)
    except ValueError as e:
        raise ValueError(f"Invalid numeric value in input: {e}") from e
    
    return value * units_map[unit_lower]

def process_distances(distance_strings: List[str]) -> None:
    """
    Processes a list of distance strings, converts them to meters, 
    and prints the results.
    
    Args:
        distance_strings (List[str]): A list of input distance strings.
        
    Raises:
        ValueError: If any string in the list cannot be parsed as a valid distance.
    """
    converted_distances = []
    
    for idx, dist_str in enumerate(distance_strings):
        try:
            meters = parse_distance_input(dist_str)
            converted_distances.append(meters)
            print(f"Input '{dist_str}' -> {meters:.2f} m")
        except ValueError as e:
            raise ValueError(f"Error processing input at index {idx}: {e}") from e

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user interaction.
    # These cover various formats and units for robustness testing.
    SAMPLE_INPUTS = [
        "10",           # Plain number (assumed meters)
        "5m",          # Meters explicitly stated
        "2km",         # Kilometers
        "300cm",       # Centimeters
        "75mi",        # Miles
        "invalid",     # Invalid input to test error handling logic if run with different data, 
                       # but here we include a valid one for the sample block.
    ]

    # Filter out intentionally invalid samples from this specific hard-coded list 
    # to ensure successful execution without crashing on bad inputs in the demo context.
    VALID_SAMPLES = [s.strip() for s in SAMPLE_INPUTS if not (not re.match(r'^(\d+(?:\.\d+)?)', s))]

    process_distances(VALID_SAMPLES)