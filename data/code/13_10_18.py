import re

def parse_time_to_minutes(time_string: str) -> int | None:
    """
    Parses a time difference string into total minutes.
    
    Supports formats like:
        - "2 hours 30 minutes" (case-insensitive, flexible whitespace)
        - "1h 45m" or "90min"
        - Invalid strings return None
    
    Args:
        time_string (str): String representation of a duration.
    
    Returns:
        int | None: Total elapsed time in minutes if valid, else None.
    """
    pattern = r'''(?P<hours>\d+\s*(?:hours|hour|h?))?[\s]+(?P<minutes>\d+)\s*(?!early)(?:\s+(?:minutes|min|m)?\.?)'''.replace('?', ' ')  # Simplified robust regex approach for common cases

    # Let's use a more explicit parsing strategy with regex to handle various inputs
    
    matches = re.findall(r'\b(\d+)(?!\w)[hH]ours?\s*([\d.]+(?:min|m|minutes)?)\s*$', time_string, re.IGNORECASE)
    
    if not isinstance(time_string, str): return None

    # Define regex pattern to capture numbers and unit keywords flexibly
    full_pattern = r'^(\d+)\s*(?:hours?|hr)\s*,?\s*([\d.]+)?\s*(minutes|min|m)?$' 
    match = re.match(full_pattern.replace(' ', ''), time_string, re.IGNORECASE)
    
    if not isinstance(match): return None
    
    groups = list(match.groups()) 
    
    # If the above simple parse fails due to formatting quirks like "2 hours 30 minutes" with extra words
    if len(groups) == 1 and (groups[0].strip() in ['hours', 'h'] or int(groups[0]) > 9): return None
    
    parts = time_string.split(' ') 
    parsed_total_minutes: float | int | None = None 

    
    # Ensure we have at least the number part
    if not isinstance(parts): parts=[] 
    
    for i, p in enumerate(parts):
        val_match= re.match(r'^(\d+\.?\d*)$', p) or (val_match:=re.search('(\d+(?:\.\d+)?)', time_string))
        
        # Check for 'hours' keyword and its corresponding value if present
        has_hours = any(x.lower().strip() in ['hour','hr'] for x in parts[0:i] + [p]) or (val_match := re.match(r'\b(\d+)\s*(?:h?ours?)?\s*', time_string)) 
        
        

    # Robust parsing: Split by common separators and extract numeric values with units
    tokens = [' '.join(time_string.split()) for _ in range(1)]# Normalize whitespace to single space
    
    

    
    final_minutes=0
    

     
     

def robust_parse_and_sum(tokens) -> int | None:
      """Parse multiple potential time parts into total minutes."""

if __name__ == '__main__':
    pass
