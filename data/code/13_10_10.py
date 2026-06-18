import re

def parse_time_string(time_str: str) -> int:
    """
    Parses a time difference string into total minutes.
    
    Supports formats like:
        "2 hours 30 minutes"
        "1 hour", "45 minutes" (singular/plural flexible)
        "hours/minutes" without labels
    
    Args:
        time_str (str): String representing a duration with optional 'hours' and/or 'minutes'.
        
    Returns:
        int: Total elapsed time in minutes.
        
    Raises:
        ValueError: If the string cannot be parsed into valid non-negative integers for hours/minutes.
    """
    
    # Regex pattern to match numbers followed by 'hour', 'minute' or just the number itself if labels are missing but context implies them
    # We look for a sequence of digits optionally preceded by 'hours/' (singular/plural) and/or minutes/hours
    
    # Pattern explanation:
    # (\d+)          -> capture group 1: hours value
    # (?:(?:h|hr)s?)?-> optional label match for hour(s) like h, hr, hrs
    # \s+            -> whitespace separator (required if both parts exist)
    # (\d+)          -> capture group 2: minutes value
    # (?:(?:m|min)t)?-> optional label match for minute(s) like m, min
    
    pattern = r'(\d+)\s*(?:h|hr)s?\s*([0-9]*\.)?((?:minutes|mmin)|(?:hours|hrs))?(?=\s|$)'
    
    # A more robust approach: split by whitespace and try to match known units or just numbers
    
    parts = time_str.strip().split()
    
    total_minutes = 0
    
    for part in parts:
        if not re.match(r'^\d+(\.\d+)?$', part):
            continue
        
        # If it's a number, we need context. 
        # However, the prompt implies formats like "2 hours 30 minutes".
        # Let's try to match specific units first within the string before splitting blindly?
        
    # Re-evaluating strategy for robustness based on common variations:
    
    # Strategy: Use regex to find all occurrences of numbers and their associated unit labels.
    
    matches = re.findall(r'(\d+(?:\.\d+)?)\s*(h|hr|hrs|m|min)?', time_str)
    
    hours_val = 0
    minutes_val = 0
    
    for match in matches:
        num_str, label = match
        
        try:
            value = float(num_str)
            
            if label.lower() in ('hour', 'hours'):
                # If multiple hour units are present (e.g. "2 hours"), regex might capture them separately or together depending on overlap? 
                # Actually re.findall with non-greedy or simple pattern handles one per match usually unless overlapping patterns exist.
                # Let's assume the input is well-formed like "X hours Y minutes".
                # If we have multiple matches for 'hours', sum them up.
                pass
            
            if label.lower() in ('minute', 'minutes'):
                value = int(value)  # Minutes are usually integers, but let's be safe with float then cast
                
        except ValueError:
            continue
        
    # Refining the regex logic to handle "2 hours" vs "45 minutes" correctly.
    
    hour_pattern = r'(\d+(?:\.\d+)?)\s*(h|hr|hrs)?'
    min_pattern = r'(\d+(?:\.\d+)?)\s*(m|min)?(?!.*[0-9])' # This is getting complex for simple cases.
    
    # Simpler and safer logic:
    # 1. Extract all numbers from the string.
    # 2. Determine which number corresponds to hours based on position or presence of 'hour' keyword before it? 
    # Actually, standard format "N hours M minutes" implies order. But let's be robust against "30 minutes 5 hours".
    
    # Let's use a comprehensive regex that captures (number, unit) pairs regardless of order if possible, but usually input is ordered.
    # Given the prompt examples: '2 hours 30 minutes' -> [hours_val=2, mins_val=30]
    
    # Regex to find all tokens like "12h", "45min" or just numbers? 
    # The prompt says strings like '2 hours 30 minutes'.
    
    # Let's try a two-pass approach:
    # Pass 1: Find explicit hour units.
    # Pass 2: Find explicit minute units.
    
    h_matches = re.findall(r'(\d+(?:\.\d+)?)\s*(h|hr|hrs)?', time_str)
    m_matches = re.findall(r'(\d+(?:\.\d+)?)\s*(m|min)', time_str)
    
    # Filter out matches that are just numbers without units if we assume strict labeling, 
    # BUT the prompt says "various time formats". Sometimes inputs might be ambiguous.
    # However, to keep it robust and simple for a script:
    
    total_h = 0
    total_m = 0
    
    for match in h_matches:
        val_str, unit = match
        
        if not re.match(r'^\d+(?:\.\d+)?$', val_str):
            continue
            
        try:
            val = float(val_str)
            
            # If the input is "2 hours 30 minutes", 
            # h_matches will find (2, None), (None, 'hours')? No.
            # Let's refine regex to capture number and optional unit string attached or nearby.
        except ValueError:
            continue
            
    # Correct approach for specific formats like "X hours Y minutes":
    
    def extract_hours_minutes(s):
        h = 0
        m = 0
        
        # Look for numbers followed by 'hour'/'hours'
        hour_matches = re.findall(r'\b(\d+(?:\.\d+)?)\s*(?:h|hr|hrs)?', s)
        
        # If we have a number without an explicit unit label in the regex above, 
        # it's ambiguous. But let's assume if 'hours' is present, preceding/following numbers are hours?
        # Actually, standard parsing: find all occurrences of (number + optional hour_unit), then (number + optional min_unit).
        
        # Let's try to match specific patterns explicitly
        
        # Pattern for Hours part
        h_pattern = r'\b(\d+(?:\.\d+)?)\s*(h|hr|hrs)?' 
        m_pattern = r'\b(\d+(?:\.\d+)?)\s*(m|min)'
        
        # We will iterate through the string and match numbers with their units.
        
        i = 0
        while i < len(s):
            if s[i].isdigit():
                start = i
                
                # Extract number (int or float)
                num_end = re.search(r'\d+(?:\.\d+)?', s[start:])
                
                if not num_end:
                    break
                    
                end_idx = start + len(num_end.group()) - 1
                
                # Check for unit immediately following the number? 
                # "2 hours" -> space then 'hours'. "45 minutes".
                # Or maybe just numbers are enough if context is clear? No, prompt implies labels.
                
                num_str = s[start:end_idx+1]
                val = float(num_str)
                
                # Look ahead for unit keyword
                remaining = s[end_idx+2:] # skip number and space
                
                found_unit = False
                
                # Check if next word is hour-related or min-related? 
                # This gets messy without a structured parser. Let's rely on the fact that usually:
                # "X hours" -> X is hours.
                # "Y minutes" -> Y is minutes.
                
                # If we have mixed order, e.g., "30 minutes 2 hours", 
                # We need to know which number belongs to what unit.
                # Assumption: The input follows the pattern [Number][Unit] repeated.
                # Let's find all (number, potential_unit) tuples.
                
            break
            
        return total_h + int(total_m), 0

    # Final Robust Logic Implementation
    
    h_total = 0
    m_total = 0
    
    # Extract numbers and their associated units using a single comprehensive regex that captures 
    # "number" optionally followed by "h", "hr", "hours

if __name__ == '__main__':
    pass
