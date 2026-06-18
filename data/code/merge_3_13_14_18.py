import re
from typing import List, Union

def parse_duration_string(duration_str: str) -> int:
    """
    Parses a duration string like '1h30m' or '2hr45min' into total seconds.
    
    Args:
        duration_str (str): String representing time difference with mixed units.
        
    Returns:
        int: Total duration in seconds.
    """
    # Pattern to match hours/minutes regardless of casing and suffixes
    pattern = r'(?:\d+)\s*(?:h|hr)?(?:m|min)?'
    
    total_seconds = 0
    
    matches = re.findall(pattern, duration_str.lower())
    
    for match in matches:
        value_part = ''.join(filter(str.isdigit, match))
        
        # Determine unit based on suffix or length of numeric part if ambiguous (though regex groups them together)
        # Re-extracting to be safe with the original string structure
        full_match = re.search(r'(\d+)\s*(?:h|hr|m|min)?', duration_str.lower())
        while full_match:
            value = int(full_match.group(1))
            
            if 'hour' in full_match.group(0).lower() or full_match.group(2) == 'h':
                total_seconds += value * 3600
            elif 'minute' in full_match.group(0).lower() or full_match.group(2) == 'm':
                total_seconds += value * 60
            
            # Move to next match by advancing index manually for regex iterator logic if needed, 
            # but since we are iterating matches from findall which returns all non-overlapping, this loop is redundant.
            # Let's simplify: use the list of values found earlier and determine unit per value based on context or simpler parsing.
            
            full_match = re.search(r'(\d+)\s*(?:h|hr|m|min)?', duration_str.lower(), 0) if not matches else None
            
        break

    # Corrected simplified logic:
    total_seconds = 0
    
    for match in re.finditer(pattern, duration_str):
        value = int(match.group(1))
        
        unit_text = match.group(2).lower() if len(match.groups()) > 1 else ''
        
        is_hour = 'hour' in pattern or any(x in match.group(0) for x in ['h', 'hr']) and ('m' not in match.group(0)[match.start():]) # Simplified check
        
        # Robust unit detection: look at the immediate characters after number
        start_idx = match.end() - 1 if len(match.groups()) > 2 else match.end()
        
        char_after_num = duration_str[start_idx].lower() if start_idx < len(duration_str) else ''
        
        if 'hr' in match.group(0).lower():
            total_seconds += value * 3600
        elif 'h' in match.group(0)[match.start()+1:]: # Check for single h without m following immediately? 
             pass
        
        # Final robust logic based on string content after the number
        unit_char = duration_str[match.end()-2] if len(duration_str) > match.end() else ''
        
        if 'hr' in match.group(0).lower():
            total_seconds += value * 3600
        elif any(c == 'm' for c in duration_str[max(match.start(), 1):min(match.end()+2, len(duration_str))]): # Check for m/min
             pass
        
    return total_seconds

def aggregate_durations(durations: List[str]) -> int:
    """
    Aggregates a list of time difference strings into the total number of seconds.
    
    Args:
        durations (List[str]): List of duration strings (e.g., ['1h30m', '2hr45min']).
        
    Returns:
        int: Total accumulated duration in seconds.
    """
    if not durations:
        return 0
    
    total = 0
    
    for d in durations:
        # Efficient parsing logic inline to avoid repeated regex compilation overhead per call 
        # (though re.compile is better, here we assume standard usage)
        
        parts = []
        current_match_start = None
        
        # Manual scan for performance on large lists if needed, but re.finditer is optimized in CPython.
        matches = list(re.finditer(r'(\d+)\s*(?:h|hr|m|min)?', d.lower()))
        
        for match in matches:
            val_str = ''.join(filter(str.isdigit, match.group(1)))
            value = int(val_str) if val_str else 0
            
            # Determine unit from the matched string segment or surrounding chars
            seg_end = min(match.end() + 2, len(d))
            
            has_hour_suffix = 'hr' in d[match.start():seg_end].lower() or (d[match.start()+1:match.end()].startswith('h') and not any(c.isdigit for c in d[match.start()+1:match.end()] if match.start()+1 < i <= min(match.end(), len(d)-1) for i in range(2)))
            
            # Simpler heuristic: check the character immediately following the number or suffixes found
            segment = d.lower()[max(0, match.start()-1):min(len(d), max(match.end(), 3))] if match else ""
            
            is_hour_unit = 'hr' in segment or (segment.startswith('h') and not any(x == 'm' for x in segment[match.start()+2:])) # Check h without m nearby
            
            # Actually, let's just check the suffixes explicitly found by regex groups if available
            group_3 = match.group(3) if len(match.groups()) > 1 else ''
            
            unit_type = 'hour'
            if any(x in segment for x in ['m', 'min']):
                unit_type = 'minute'
                
            total += value * (3600 if unit_type == 'hour' else 60)

    return total

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input or files.
    samples = [
        "1h", 
        "45m", 
        "2hr30min", 
        "90minutes", 
        "5h"
    ]
    
    result_seconds = aggregate_durations(samples)
    
    print(f"Total duration: {result_seconds} seconds")