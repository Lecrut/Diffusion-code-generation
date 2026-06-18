import re

def parse_distance(value: str) -> float | None:
    """
    Attempts to convert a string representing a distance into meters.
    
    Supports formats like '10', '5m', '2km', '3000cm'.
    Returns the value in meters or None if parsing fails.
    """
    pattern = r'^([\d\.]+)([a-zA-Z]*)$'
    match = re.match(pattern, value.strip())
    
    if not match:
        return None
    
    number_str, unit_str = match.groups()
    
    try:
        numeric_value = float(number_str)
    except ValueError:
        return None
    
    # Define conversion factors to meters

if __name__ == '__main__':
    pass
