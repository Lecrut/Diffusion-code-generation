import re

def parse_distance(input_str):
    """
    Parses a string representing a distance with optional unit suffix.
    
    Supported units: m (meters), km (kilometers)
    Returns float value in meters, or None if invalid format.
    Raises ValueError for unparseable strings.
    """
    # Pattern to match number followed by optional 'km' or 'm'
    pattern = r'^([\d.]+)\s*(?:km|m)?$'
    
    match = re.match(pattern, input_str.strip())
    if not match:
        return None
    
    try:
        value = float(match.group(1))
        
        unit_suffix = match.group(2) or 'm'  # Default to meters
        
        if unit_suffix == 'km':
            return value * 1000.0
        elif unit_suffix == 'm':
            return value
        else:
            raise ValueError(f"Unsupported unit suffix: {unit_suffix}")
    except (ValueError, TypeError):
        return None

def process_distances(input_strings):
    """
    Processes a list of distance strings and returns values in meters.
    
    Args:
        input_strings: List of strings representing distances
        
    Returns:
        Tuple of (success_count, failed_indices) where success is count 
        of successfully parsed inputs and failed_indices are indices that failed parsing
    """
    results = []
    for idx, s in enumerate(input_strings):
        result = parse_distance(s)
        if result is not None:
            results.append(result)

if __name__ == '__main__':
    pass
