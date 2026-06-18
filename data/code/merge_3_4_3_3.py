import re

def parse_distance_string(s: str) -> float | None:
    """
    Parses a string representing a distance in any common unit to meters.
    
    Supported formats (case-insensitive):
        - <number> m, M, km, Km, cm, Cm, mm, Mm (e.g., "5", "3km", "2cm")
        - <number>.<fraction> ... same units
    
    Returns the value in meters or None if invalid.
    
    Raises: ValueError on format errors that cannot be silently ignored by returning None.
    """
    pattern = r'^(\d+\.?\d*)\s*([a-zA-Z]+)?$'
    match = re.match(pattern, s.strip())

    if not match:
        return None

    value_str = match.group(1)
    unit_str = match.group(2).lower() if match.group(2) else 'm'

    try:
        value = float(value_str)
    except ValueError:
        return None

    # Define conversion factors to meters (base unit is meter, m)
    units_to_factor = {
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'um': 1e-6,   # micrometer (optional extension for robustness)
        'nm': 1e-9,   # nanometer (optional extension for robustness)
    }

    if unit_str not in units_to_factor:
        return None

    meters = value * units_to_factor[unit_str]
    
    # Basic sanity check to avoid absurdly large/small numbers that might indicate parsing error
    if abs(meters) > 1e20 or (abs(meters) < 1e-30 and not unit_str.startswith('nm')):
        return None

    return meters

def process_distances(input_lines):
    """
    Takes a list of input strings, parses each as a distance to meters.
    
    Returns a dictionary mapping original string -> parsed value in meters or 'INVALID' for unparseable lines.
    """
    results = {}
    valid_count = 0
    
    for line in input_lines:
        if not line.strip():
            continue
            
        result = parse_distance_string(line)
        
        if result is None:
            # Treat as invalid format, but we'll log it or handle gracefully. 
            # Since the task says "validates", let's mark clearly.
            results[line] = 'INVALID'
        else:
            valid_count += 1
            results[line] = round(result, 6)  # Round to avoid floating point noise
    
    return results

if __name__ == '__main__':
    # Hard-coded sample values as per instructions. 
    # No user input, command-line arguments, network access, or pre-existing files required.
    
    SAMPLE_INPUTS = [
        "10",                 # 10 meters
        "5km",               # 5 kilometers -> 5000m
        "2cm",               # 2 centimeters -> 0.02m
        "3mm",               # 3 millimeters -> 0.003m
        "invalid text"       # Should be marked invalid
    ]

    parsed_results = process_distances(SAMPLE_INPUTS)

    print("Parsed Distances (converted to meters):")
    for original, value in parsed_results.items():
        if isinstance(value, float):
            print(f"{original} -> {value}")
        else:
            print(f"{original} -> INVALID FORMAT")