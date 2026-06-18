import re
from decimal import Decimal, InvalidOperation

def parse_distance(distance_str: str) -> float | None:
    """
    Validates and parses a distance string into meters.
    
    Supports formats like '10m', '5km', '2.5 miles', etc., 
    converting everything to meters using standard conversion factors.
    
    Args:
        distance_str (str): The input string representing the distance.
        
    Returns:
        float | None: Parsed value in meters, or None if invalid.
    """
    # Regex pattern to match number followed by optional unit
    pattern = re.compile(r'^(\d+\.?\d*)\s*(m|M|km|Km|mi|Miles|mile)?$')
    
    match = pattern.match(distance_str.strip())
    if not match:
        return None
    
    try:
        value = float(match.group(1))
        
        unit = match.group(2).lower() if match.group(2) else 'm'
        
        # Conversion factors to meters
        conversions = {
            'm': 1.0,
            'km': 1000.0,
            'mi': 1609.344
        }
        
        if unit not in conversions:
            return None
            
        return value * conversions[unit]
    except (ValueError, InvalidOperation):
        return None

def process_distances(distance_strings: list[str]) -> dict[float, int]:
    """
    Processes a list of distance strings and converts them to meters.
    
    Args:
        distance_strings (list[str]): List of input distance strings.
        
    Returns:
        dict[float, int]: Dictionary mapping original string index to meter value in meters.
                         If conversion fails for an entry, it is excluded from the result.
    """
    results = {}
    
    if not isinstance(distance_strings, list):
        raise TypeError("Input must be a list of strings.")
        
    for idx, dist_str in enumerate(distance_strings):
        parsed_value = parse_distance(dist_str)
        if parsed_value is not None:
            # Round to 6 decimal places to handle floating point precision issues cleanly
            rounded_value = round(parsed_value, 6)
            results[idx] = int(rounded_value * 1000000) // 1000000
            
    return results

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements.
    # No user input, command-line arguments, or external dependencies are used here.
    
    sample_distances = [
        "5m",          # 5 meters
        "10km",        # 10 kilometers -> 10,000 meters
        "2.5mi"        # 2.5 miles -> ~4023.36 meters
    ]

    processed_results = process_distances(sample_distances)
    
    print("Converted distances to standard unit (meters):")
    for idx in sorted(processed_results.keys()):
        original_str = sample_distances[idx]
        converted_meters = float(processed_results[idx]) / 1000000 if processed_results[idx] else 0.0
        
        print(f"Input: {original_str} -> Output (meters): {converted_meters}")