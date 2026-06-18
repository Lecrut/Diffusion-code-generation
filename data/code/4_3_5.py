import re

def parse_distance(distance_str: str) -> float:
    """
    Parse a distance string into its numeric value in meters (km, m, cm).
    
    Supports formats like "10m", "5.2 km", "-3cm".
    Invalid formats raise an exception with a clear message.
    
    Args:
        distance_str (str): The input distance string.
        
    Returns:
        float: Distance in meters.
        
    Raises:
        ValueError: If the format is invalid or conversion fails.
    """
    if not isinstance(distance_str, str) or not distance_str.strip():
        raise ValueError("Input must be a non-empty string.")

    # Define unit patterns with their multiplication factors for meters (1 km = 1000 m, etc.)
    units_factors = {
        'km': float(1e3),
        'm': float(1.0),
        'cm': float(1e-2)
    }

    # Regex pattern to match optional sign, digits with decimals, unit char (case-insensitive).
    pattern = r'^(\+|-)?\d*\.?\d+\s*(km|m|cm)$'
    
    if not re.match(pattern, distance_str.strip(), flags=re.IGNORECASE):
        raise ValueError(f"Invalid format: '{distance_str}'. Expected 'Xm', 'X km', or 'X cm'.")

    # Extract numeric part and unit from the string. We use regex sub to normalize 
    # uppercase units for consistent lookup while capturing groups via a callback-like approach
    # However, since re.sub can't easily do conditional capture without flags in older Python versions,
    # we'll split by whitespace first then check end of string char case-insensitively.

    value_str = distance_str.strip()
    
    # Find the last non-space character to determine unit (case insensitive)
    clean_val = "".join(filter(str.isalnum, value_str))
    unit_char = value_str.split()[-1].lower().strip('km m cm') if " ".join(value_str.split()) else "" 
    # Actually simpler: just extract the number and the last alphanumeric char that is a unit.
    
    # Let's do manual parsing for robustness after regex validation to ensure we get clean parts
    
    # Re-extract cleanly based on validated structure
    sign = 1 if value_str[0] == '+' else (-1 if value_str.startswith('-') else 1)

if __name__ == '__main__':
    pass
