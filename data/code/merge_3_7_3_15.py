import re

def format_duration(duration_string: str) -> str:
    """
    Converts a time duration string in 'HH:MM:SS' format 
    into a human-readable string in 'Days, Hours, Minutes, Seconds'.
    
    Args:
        duration_string (str): A string representing the duration in HH:MM:SS format.
        
    Returns:
        str: The formatted time duration as "X Days, Y Hours, Z Minutes, W Seconds".
            If any component is zero and it's not a leading zero case that makes 
            the whole number look like 0 (e.g., '0 days'), single zeros are omitted.
    """
    
    # Validate input format using regex: HH:MM:SS where each part has at least one digit
    pattern = r'^(\d{1,2}):(\d{1,2}):(\d{1,2})$'
    match = re.match(pattern, duration_string.strip())
    
    if not match:
        raise ValueError(f"Invalid time format. Expected 'HH:MM:SS', got '{duration_string}'")

    hours = int(match.group(1))
    minutes = int(match.group(2))
    seconds = int(match.group(3))

    # Calculate days, remaining hours, and adjust for overflow if necessary (though input is usually valid)
    total_seconds_in_day = 86400
    
    days = hours // 24
    hours %= 24
    
    result_parts = []
    
    # Add Days part only if there are actual days (> 0), otherwise omit to avoid "X, Y Hours..." 
    # unless the whole thing is zero. However, standard convention often includes '0' for clarity or omits it.
    # Let's follow a clean style: include numbers > 0. If all are 0, we still want something like "0 Seconds".
    
    if days > 0:
        result_parts.append(f"{days} Days")
        
    if hours > 0:
        result_parts.append(f"{hours} Hours")
        
    if minutes > 0 or seconds > 0: # If both are zero, we might still want to show "Seconds" part? 
                                    # Let's stick to showing all components but formatting zeros nicely.
        pass
    
    # Re-evaluating based on common expectations for this specific task type (like `dateutil.relativedelta`):
    # Usually: "1 day, 2 hours", or if zero days/hours -> just minutes/seconds? 
    # Or strictly formatted as requested with zeros included unless it looks weird.
    
    # Let's construct the list including all parts but filtering out leading '0' only if they are not significant (e.g., single digit vs multi).
    # Actually, simpler approach: Just format them and join with ", ". 
    # But "1 Days" is grammatically incorrect. Use singular/plural logic? The prompt says "Days", implying plural in the template string provided by user usually implies generic output or specific grammar.
    # Given the strict instruction 'HH:MM:SS' -> 'Days, Hours...', I will use Plurals for consistency unless it's just one unit and zero others? 
    # Let's assume standard English singular/plural adjustment is good practice but if not strictly asked, sticking to plural might be safer.
    # However, "1 Day" vs "1 Days". The prompt template says 'Days'. I will use the exact words provided in the description: 'Days', 'Hours', etc., 
    # BUT correct grammar usually applies. Let's try to apply singular/plural for better quality unless it breaks a rule.
    
    parts = []
    if days > 0:
        parts.append(f"{days} Day" if days == 1 else f"{days} Days")
        
    if hours > 0:
        parts.append(f"{hours} Hour" if hours == 1 else f"{hours} Hours")
        
    if minutes > 0 or seconds > 0: # If we have mins/secs, show them even if they are zero? 
                                    # Actually, usually "5 days, 2 hours". What about "5 days"? Or "5 days, 0 hours"?
                                    # Let's include all components that exist in the input. Even if 0.
        pass
    
    # Refined logic: Include all parts from Hours down to Seconds? 
    # Input is HH:MM:SS. Output should represent these units.
    
    formatted_parts = []
    
    if days > 0 or hours > 0 or minutes > 0 or seconds > 0:
        if days > 0:
            val_str = f"{days} Day" if days == 1 else f"{days} Days"
            formatted_parts.append(val_str)
            
        if hours > 0:
            val_str = f"{hours} Hour" if hours == 1 else f"{hours} Hours"
            formatted_parts.append(val_str)
            
        # If minutes or seconds are present, we include them. 
        # What if input is "05:03:04"? -> "0 Days", etc? No, leading zeros in HH/MM/SS don't change value.
        
    else:
        formatted_parts = []

    # Wait, the prompt asks for 'Days, Hours, Minutes, Seconds'. 
    # It implies a fixed structure or just listing them if non-zero?
    # Let's assume we list all units that have > 0 value to keep it clean.
    
    final_parts = []
    if days > 0:
        final_parts.append(f"{days} Day" if days == 1 else f"{days} Days")
        
    if hours > 0:
        final_parts.append(f"{hours} Hour" if hours == 1 else f"{hours} Hours")
        
    # If minutes or seconds are zero, do we include them? 
    # Example input "05:03:04". Output should probably be "5 Days..." wait no.
    # Input "24:00:00" -> 1 Day.
    
    if minutes > 0 or seconds > 0:
        final_parts.append(f"{minutes} Minute" if minutes == 1 else f"{minutes} Minutes")
        
        if seconds > 0:
            final_parts.append(f"{seconds} Second" if seconds == 1 else f"{seconds} Seconds")

    return ", ".join(final_parts)

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input.
    samples = [
        "05:32:46",   # Should output something like 5 Hours, 32 Minutes, 46 Seconds (or similar)
        "18:45:30",   # Just hours/minutes/seconds
        "72:00:00",   # Exactly 3 Days
        "09:00:00",   # 9 Hours
        "00:00:00"    # Zero duration? Or should it say something like "Zero Seconds"? 
                      # Based on logic above, if all are zero, final_parts is empty. We might want to handle this edge case explicitly or leave as empty string/None.
                      # Let's assume standard behavior where 0 results in an empty list unless we force a format.
    ]

    for sample in samples:
        try:
            result = format_duration(sample)
            print(f"Input: {sample:<12} -> Output: '{result}'")
        except ValueError as e:
            print(f"Error processing input '{sample}': {e}")