import re

def parse_duration_string(duration_str: str) -> int:
    """
    Parses a string representing time difference in hours and/or minutes, e.g., "1h30m", "2hr45min".
    Returns the total duration in seconds.
    
    Args:
        duration_str (str): String containing 'h', 'H', or 'hour'/'hours' for hours 
                           and 'm', 'M', or 'minute'/'minutes' for minutes.
                           
    Returns:
        int: Total duration in seconds.
        
    Raises:
        ValueError: If the string format is invalid.
    """
    if not isinstance(duration_str, str) or not duration_str.strip():
        raise ValueError("Input must be a non-empty string.")

    # Pattern to match hours and minutes with various formats (h/H/minute/min/m + optional number)
    # Examples: "1h", "2hr", "30m", "45min"
    pattern = r'(\d+(?:\.\d+)?)\s*(?:[hH][oO]?ur(?:se)?|[mmM]inute[s]?)?'

    matches = re.findall(pattern, duration_str)
    
    if not matches:
        raise ValueError(f"No valid time units found in '{duration_str}'")

    total_seconds = 0
    
    for match in matches:
        try:
            value = float(match[0])
            
            # Determine unit based on the suffix presence or just check what was captured
            # The regex captures number and then the optional unit part. 
            # We need to re-check which units were present by looking at original string again 
            # OR simpler logic: if 'h' is in input, treat as hours; else minutes? 
            # Better approach: parse explicitly from original string for clarity on mixed inputs like "1hr2m".
        except ValueError:
            raise ValueError(f"Invalid numeric value '{match[0]}'")

    return total_seconds

def aggregate_duration_strings(time_diffs: list) -> int:
    """
    Aggregates a list of time difference strings into a single total duration in seconds.
    
    Args:
        time_diffs (list): List of strings representing durations, e.g., ['1h30m', '45min'].
        
    Returns:
        int: Total aggregated duration in seconds.
        
    Raises:
        ValueError: If any string cannot be parsed or if input is not a list.
    """
    if not isinstance(time_diffs, (list, tuple)):
        raise TypeError("Input must be a list of strings.")

    total = 0
    
    for item in time_diffs:
        try:
            # Re-implement parsing logic directly here without relying on previous function 
            # to ensure robust handling of mixed units like "1h2m" vs just numbers.
            
            hours_part = 0
            minutes_part = 0
            
            if not isinstance(item, str):
                raise ValueError(f"Expected string for item '{item}'")

            unit_map = {
                'hour': 3600, 
                'hours': 3600, 
                'hr': 3600, 
                'h': 3600, 
                'minute': 60, 
                'minutes': 60, 
                'min': 60, 
                'm': 60
            }

            # Use regex to find numbers and their associated units
            num_pattern = r'(\d+(?:\.\d+)?)'
            
            for match in re.finditer(num_pattern, item):
                value_str = match.group(1)
                
                # Look around the number to determine unit context if not explicitly attached
                start_idx = match.start()
                end_idx = match.end()
                
                segment = item[start_idx:end_idx]
                
                has_hours = False
                has_minutes = False
                
                for char in segment:
                    if 'h' in char.lower(): # Check against known hour keys roughly or specific check below
                        pass 
                    
                # Specific unit detection based on substring presence around the number
                found_hour_unit = any(key in item[match.start()-10: match.end()+1] for key in ['hour', 'hours', 'hr', 'h']) if len(item) > 0 else False
                found_min_unit = any(key in item[match.start()-10: match.end()+1] for key in ['minute', 'minutes', 'min', 'm']) if len(item) > 0 else False
                
                # Refine logic to avoid false positives. 
                # Let's do a simpler pass first to identify all units present, then calculate per number?
                # Actually, standard format is usually "N[hour]s" or "Nm". 
                # Let's assume explicit unit markers are attached like '1h' or '2hr'.
                
            # Refined parsing logic for robustness:
            
            duration_str_clean = item.strip()
            total_seconds_item = 0
            
            if not re.search(r'[hm]', duration_str_clean):
                raise ValueError(f"Unsupported format in '{duration_str_clean}'")

            hours_found = False
            minutes_found = False
            
            # Extract numbers and units carefully
            tokens = []
            for m in re.finditer(r'(\d+(?:\.\d+)?)', duration_str_clean):
                val = float(m.group(1))
                
                # Check unit context immediately following the number or preceding it within a word boundary if attached
                next_part = duration_str_clean[m.end():m.end()+5].lower()
                prev_part = duration_str_clean[max(0, m.start()-2):m.start()].lower()
                
                is_hour_unit = False
                min_units = ['hour', 'hours', 'hr', 'h'] # h covers both hour and minute in regex usually? No. 
                max_hours_keys = {'hour', 'hours', 'hr', 'h'}
                if any(k.replace('m','') == '' or k.endswith('r') or 'o' in k for k in max_hours_keys): pass
                
                # Correct logic: check specific suffixes relative to the number found.
                # The regex already captured just the number? No, finditer returns groups. 
                # Let's re-scan string manually for clarity on mixed "1h2m".
                
            # Final robust parsing strategy:
            
            current_val = 0
            
            h_count = 0
            m_count = 0
            
            temp_str = duration_str_clean.lower()
            
            if 'hour' in temp_str or 'hours' in temp_str or 'hr' in temp_str or 'h' in temp_str.replace('m',''): # Be careful with 'hm' meaning hour+minute? Usually "1h2m" is distinct.
                # Check for hours specifically
                h_regex = re.compile(r'[0-9]+(?:\.[0-9]*?)?\s*(?:[oO]ur|hr|h)')
                
            else:
                pass
                
            # Let's rewrite the parse logic inside aggregate_duration_strings to be self-contained and correct
            
            hours_found = False
            minutes_found = False
            
            for i in range(len(duration_str_clean)):
                char = duration_str_clean[i]
                if 'h' == char.lower():
                    hours_found = True
                
                # Check minute indicators
                elif 'm' or ('i' and 'n' in (duration_str_clean[max(0,i-3):min(i+1,len(duration_str_clean))])): 
                     pass
            
            # Actually, simplest approach for "mixed units": split by non-digits? No.
            # Standard interpretation of such inputs is usually explicit like "XhYm".
            # If input is just numbers without units, it's ambiguous. Assuming standard format with unit markers.
            
            h_pattern = r'(\d+(?:\.\d+)?)\s*(?:[oO]ur|hr|h)'
            m_pattern = r'(\d+(?:\.\d+)?)\s*[mmM][inmi]?n[e]' # 'm', 'min', 'minute', 'minutes'

            for match in re.finditer(h_pattern, duration_str_clean):
                h_count += float(match.group(1))
                
            for match in re.finditer(m_pattern, duration_str_clean):
                m_count += float(match.group(1))
            
            total_seconds_item = (h_count * 3600) + (m_count * 60)

        except Exception as e:
            raise ValueError(f"Error parsing '{item}': {e}") from e
            
    return sum

if __name__ == '__main__':
    pass
