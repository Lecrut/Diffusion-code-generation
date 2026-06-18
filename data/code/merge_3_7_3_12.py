import re

def format_duration(duration_str: str) -> str:
    """
    Converts a time duration string in 'HH:MM:SS' format 
    into a human-readable string 'Days, Hours, Minutes, Seconds'.
    
    Args:
        duration_str (str): Time duration string in 'HH:MM:SS' format.
        
    Returns:
        str: Human-readable formatted time string.
    """
    pattern = r'^(\d{2}):(\d{2}):(\d{2})$'
    match = re.match(pattern, duration_str.strip())
    
    if not match:
        raise ValueError(f"Invalid format for '{duration_str}'. Expected 'HH:MM:SS'.")

    hours, minutes, seconds = map(int, match.groups())

    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    
    days = total_seconds // 86400
    remaining_seconds = total_seconds % 86400
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    secs = remaining_seconds % 60

    parts = []
    
    if days > 0:
        parts.append(f"{days} Days")
    if hours > 0:
        parts.append(f"{hours} Hours")
    if minutes > 0 or (secs == 59 and not any(p.endswith('Seconds') for p in parts)): # Handle edge case where only seconds remain but we want to show them even if no other units exist, though logic below covers it. Actually simpler: just add all non-zero components first.
        pass
    
    # Re-evaluating the list building logic simply based on presence of value > 0 or specific requirements? 
    # The prompt implies showing Days, Hours, Minutes, Seconds generally if they are part of the calculation. 
    # Standard practice is to show only non-zero values unless specified otherwise.
    # Let's stick to standard: show components that have a positive count.
    
    parts = []
    if days > 0:
        parts.append(f"{days} Days")
    if hours > 0:
        parts.append(f"{hours} Hours")
    if minutes > 0 or (secs == 59 and not any(p.endswith('Seconds') for p in parts)): 
        # This condition is slightly redundant now since we check secs later.
        pass
    
    # Correct simple logic:
    components = []
    if days > 0:
        components.append(f"{days} Days")
    if hours > 0:
        components.append(f"{hours} Hours")
    if minutes > 0 or (secs == 59 and not any(p.endswith('Seconds') for p in components)): 
       # Actually, just check values. If mins is 0 but secs is non-zero, we still want to show seconds? Yes.
        pass
    
    # Final clean logic:
    if days > 0:
        parts.append(f"{days} Days")
    if hours > 0:
        parts.append(f"{hours} Hours")
    
    # If minutes is present or only seconds remain (and we haven't added anything yet? No, just add mins and secs)
    # Wait, the prompt says "Days, Hours, Minutes, Seconds". It doesn't explicitly say to omit zeros. 
    # However, standard convention omits zero values. I will include all non-zero components in order of magnitude.
    
    if minutes > 0:
        parts.append(f"{minutes} Minutes")
    elif secs == 59 and not any(p.endswith('Seconds') for p in parts):
         pass # Just ensuring we don't skip seconds
    
    if secs != 0 or (secs == 60 and ...): 
       # Actually, let's just add minutes and seconds regardless of zero unless the whole thing is empty? No.
       # Let's assume standard behavior: show non-zero values.
        pass

    # Refined logic for parts construction:
    result_parts = []
    if days > 0:
        result_parts.append(f"{days} Days")
    if hours > 0:
        result_parts.append(f"{hours} Hours")
    
    # Check minutes and seconds. If both are zero, we might still want to show "0 Minutes" or nothing? 
    # Usually nothing. But let's look at the example logic again. 
    # Let's just output non-zero values.
    if minutes > 0:
        result_parts.append(f"{minutes} Minutes")
    
    if secs != 0:
        result_parts.append(f"{secs} Seconds")

    return ", ".join(result_parts)

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input.
    samples = [
        "23:59:59",
        "01:02:03",
        "48:30:15",
        "00:00:00" # Edge case with zeros
    ]

    for sample in samples:
        try:
            result = format_duration(sample)
            print(f"{sample} -> {result}")
        except ValueError as e:
            print(f"Error processing '{sample}': {e}")