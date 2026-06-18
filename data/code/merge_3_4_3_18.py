import re

def parse_distance(input_str: str) -> float | None:
    """
    Parses a distance string into meters.
    
    Supports formats like '5', '10m', '2km', '3/4mi'.
    Returns None if parsing fails or input is empty.
    """
    # Regex pattern to match optional number, unit (optional), and sign
    # Matches: digits with decimals, scientific notation, fractions (e.g., 1/2)
    # Units supported for conversion: m, km, mi, ft, cm
    
    pattern = r'^([+-]?\d+\.?\d*(?:[eE][+-]?\d+)?)|(\d+/[\d]+)(\s*[a-zA-Z]*)?$'
    
    match = re.match(pattern, input_str.strip())
    
    if not match:
        return None
    
    numeric_part, fraction_part, unit_str = match.groups()
    
    # Handle empty string case (though regex should prevent this)
    if not numeric_part and not fraction_part:
        return None

    value = 0.0
    
    try:
        # Try parsing as a float first
        if numeric_part is not None:
            value = float(numeric_part)
        
        # Handle fractions like "1/2"
        elif fraction_part is not None and unit_str == '':
            parts = fraction_part.split('/')
            numerator = int(parts[0])
            denominator = int(parts[1]) if len(parts) > 1 else 1
            value = float(numerator / denominator)
        
    except ValueError:
        return None
    
    # Determine unit and convert to meters

if __name__ == '__main__':
    pass
