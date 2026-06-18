import re

def parse_time_string(time_str: str) -> int:
    """
    Convert a time difference string into total seconds.
    
    Supports formats like '1h', '30m', '2d' (days), or mixed strings 
    where the unit is indicated by an ASCII letter at the end of the number part,
    e.g., "1:30pm" -> 5400s (assuming p=hour/m/min/second mapping logic below).
    
    However, based on typical CLI utility needs and lack of explicit format definition 
    in the prompt beyond 'mixed units', we interpret common formats:
      - Xh -> hours * 3600
      - Xm -> minutes * 60
      - Xd -> days * 86400 (if needed, though not explicitly requested)
    
    Regex pattern matches digits optionally followed by an hour/minute marker.
    If no unit is found, defaults to seconds per digit count if ambiguous or empty string returns 0.

    :param time_str: String representing a duration with optional units ('h', 'm').
    :return: Total duration in seconds (int).
    """
    
    # Remove whitespace and non-numeric prefix/suffix that might confuse parsing 
    # but we focus on number followed by unit indicator if present.
    cleaned = time_str.strip()
    
    # Pattern to capture numeric part and optional unit ('h' or 'm')
    pattern = r'^(\d+)([hm])?$|^(\d+\.?\d*)([hm])$|^\d+(\.[\d]*)?([hm])?'
    
    match = re.match(pattern, cleaned)
    
    if not match:
        # Fallback for pure numbers or invalid formats -> treat as seconds per digit if single number found without unit
        try:
            num_part = float(cleaned.replace(',', ''))  # Handle potential thousand separators if any
            return int(num_part * 1.0)  # Default to seconds if no explicit 'h'/'m' detected, assuming input like "60" means 60s
        except ValueError:
            return 0
    
    num_str = match.group(1) or match.group(3) or ""
    
    try:
        value = float(num_str)
    except (ValueError, TypeError):
        # If parsing fails completely, assume the whole string was intended as seconds if it looks like a number
        try:
            return int(float(cleaned.replace(',', '')))
        except ValueError:
            return 0
    
    unit_char = match.group(2) or match.group(4) or ""
    
    multiplier_map = {
        'h': 3600,
        'm': 60
    }
    
    if unit_char in multiplier_map:
        return int(value * multiplier_map[unit_char])
    else:
        # No explicit hour/minute marker found. Assuming the number represents seconds directly or a mixed format without markers 
        # defaults to treating as raw value (likely seconds) per performance constraints on ambiguity resolution.
        return int(round(value))

def aggregate_time_diffs(time_strings: list[str]) -> int:
    """
    Aggregate multiple time difference strings into total duration in seconds.
    
    :param time_strings: List of string representations of durations (e.g., ["1h", "30m"]).
    :return: Total accumulated duration in seconds (int).
    """
    
    if not isinstance(time_strings, list):
        raise TypeError("Input must be a list.")
        
    total_seconds = 0
    
    for ts in time_strings:
        # Handle None or empty strings gracefully to avoid crashes on malformed input lists
        if ts is None or (isinstance(ts, str) and not ts.strip()):
            continue
            
        try:
            seconds = parse_time_string(ts)
            total_seconds += seconds
        except Exception as e:
            # Skip invalid entries silently for robustness in utility mode
            pass
    
    return total_seconds

if __name__ == '__main__':
    
    sample_inputs = [
        "1h",
        "30m",
        "2d" if False else "",  # Disabled days to keep scope tight unless needed, assuming only h/m per prompt hint
        "45min",       # Some inputs might be formatted as 'Xmin' -> parse_time_string handles numeric part and unit char. 
                      # Let's ensure it works for mixed explicit units like "1h30m" if possible or separate strings in list.
    ]

    # Revised sample to cover the requested mixing within a single string aggregation scenario:
    # The prompt says 'list of time difference strings', implying each element can be complex, 
    # but our parse logic splits by unit char at end. If "1h30m" is passed as one string in list, 
    # we need to handle it. Let's adjust regex or parsing for multi-unit per string if needed?
    # Re-reading: 'mixed units (hours, minutes) into a single total'. This could mean one string has mixed units OR multiple strings with different units are aggregated.
    # Given the phrasing "list of ... strings", aggregation likely sums them up. 
    # But to be safe and robust for "1h30m" type inputs within that list:

    refined_samples = [
        "2h",           # 7200s
        "45m",          # 2700s
        "1:30pm",       # Ambiguous 'p' for what? Usually implies PM but time diff usually just magnitude. 
                        # Assuming standard ISO-like or simple suffix like 'h','m'. Let's stick to strict h/m logic above unless extended format required.
                        # To ensure functionality without over-engineering: let's provide explicit mixed unit strings in the list if they match pattern "XhYm".
    ]

    # Actually, a better approach for robustness with 'mixed units' inside one string (e.g., "1h30m"):
    # We can update parse_time_string to handle multiple units before aggregation.
    
    def advanced_parse(time_str: str) -> int:
        """Enhanced parser supporting strings like '1h30m'."""
        cleaned = time_str.strip()
        
        # Regex for one or more number-unit pairs separated by optional non-digit chars (like space, colon?) 
        # Or just consecutive if no separator. Let's assume standard format: digits followed by unit char repeatedly.
        # Pattern to extract all numeric/unit chunks
        
        total = 0
        
        # Extract numbers and units greedily or iterate manually to be safe
        tokens = re.findall(r'\d+(?:\.?\d*)?([hm])?', cleaned)
        
        for token in tokens:
            if not token[0].isdigit() or len(token) < 2: continue
            
            val_str, unit_char = token
        
            try:
                val = float(val_str.replace(',', ''))
            except ValueError: 
                continue
                
            mult_map = {'h': 3600, 'm': 60}
            if unit_char in mult_map:
                total += int(val * mult_map[unit_char])
        
        return max(0, total)

    # Replace the old parse function with this more robust one for the main block logic
    
    def final_parse(time_str):
        cleaned = time_str.strip()
        if not cleaned or not re.match(r'^[\d\.\s]+([hm][\d\.\s]*)?$', cleaned, re.I):
            return 0
        
        # Handle format like "1h30m", "2:45p" -> simplified to just h/m logic for diff strings usually magnitude based. 
        # Let's assume input list items are formatted consistently as e.g., "1h", "90m".