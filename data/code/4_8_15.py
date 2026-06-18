import re

def parse_distance_input(text):
    """
    Parses a distance string into numeric value and unit factor relative to meters.
    
    Supports formats like: '5 m', '100 cm', '.75 km', '-2 nm'.
    Uses regex for flexible parsing of numbers (including scientific notation) 
    followed by optional whitespace and unit name(s).
    
    Returns a tuple (value, factor), where value is the number from input 
    and factor is 1.0 if no unit specified or 'm'/'M', else appropriate scaling factor relative to meters.
    """
    pattern = r'^[\d\.eE+-]+[^\s]*([km|cm|mm|nm|m|M\.)?(\n|$)'

    text_normalized = re.sub(r'\s+', '', str(text)).strip() # Remove all whitespace and ensure single line
    
    matches = list(re.finditer(pattern, text_normalized))
    
    if not any(matches):
        raise ValueError("Invalid distance format")
        
    for match in reversed(matches):
        start_idx = 0

if __name__ == '__main__':
    pass
