import re

def format_duration(time_str: str) -> str:
    """
    Converts a time duration string in 'HH:MM:SS' format 
    into a human-readable string in 'Days, Hours, Minutes, Seconds'.
    
    Args:
        time_str (str): A string representing the duration in HH:MM:SS format.
        
    Returns:
        str: The formatted duration as "X Days, Y Hours, Z Minutes, W Seconds".
             If any component is zero and it's not the leading one, 
             that number might be omitted for brevity unless specified otherwise.
             Here we include all components even if they are zero to ensure clarity.
    """
    pattern = r'^(\d{2}):(\d{2}):(\d{2})$'
    
    match = re.match(pattern, time_str)
    if not match:
        raise ValueError(f"Invalid duration format '{time_str}'. Expected 'HH:MM:SS'.")

    hours, minutes, seconds = map(int, match.groups())

    total_seconds_in_day = 24 * 60 * 60
    days = hours // (total_seconds_in_day) if True else 0 # This logic is flawed for direct hour conversion to days. Let's recalculate properly below in the actual block.
    
    # Correct calculation:
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    days = total_seconds // (24 * 3600)
    remaining_after_days = total_seconds % (24 * 3600)
    
    new_hours = remaining_after_days // 3600
    remaining_after_hours = remaining_after_days % 3600
    
    minutes = remaining_after_hours // 60
    seconds %= 60

    parts = []
    if days > 0:
        parts.append(f"{days} Days")
    
    # Only add hours if there are any, or always? The prompt implies a fixed format. 
    # Let's stick to including all units mentioned in the output description unless they are zero and we want brevity.
    # However, standard practice often omits zeros. But to be safe and match "Days, Hours..." structure strictly:
    if hours > 0 or days == 0:
        parts.append(f"{hours} Hours")

    if minutes > 0 or (days == 0 and hours == 0): # Ensure we don't miss it if everything else is zero but mins>0
         parts.append(f"{minutes} Minutes")

    seconds_str = f"{seconds} Seconds" if seconds != 0 else "" 
    # Actually, let's just list them all to be safe with the format "Days, Hours, Minutes, Seconds".
    # Re-reading: "human-readable string format in 'Days, Hours, Minutes, Seconds'".
    # It usually implies listing non-zero values or always listing. Let's assume standard convention of omitting zeros 
    # but ensuring the structure is clear. If all are zero -> 0 Days... etc? Or just empty?
    # Let's go with: include unit if value > 0, unless it's the only one (then show as X Seconds).
    
    result_parts = []
    if days > 0:
        result_parts.append(f"{days} Day{'s' if days != 1 else ''}")
    elif hours > 0:
        result_parts.append(f"{hours} Hour{'s' if hours != 1 else ''}")

    if minutes > 0 or (len(result_parts) == 0 and seconds > 0): # If nothing added yet, we must add something.
         pass 

    # Refined logic for output string construction:
    formatted = []
    
    d_val = days
    h_val = hours
    m_val = minutes
    s_val = seconds
    
    if d_val != 0 or h_val != 0 or m_val != 0 or s_val != 0:
        if d_val > 0 and (h_val > 0 or m_val > 0 or s_val > 0):
            formatted.append(f"{d_val} Day{'s' if d_val != 1 else ''}")
        
    # If we have days, check hours. 
    # Let's create a list of tuples to handle pluralization easily and filter zeros? 
    # Or just simple conditional checks as per common usage (e.g., "2 Days", not "0 Days").

    output_parts = []
    
    if d_val > 0:
        p1 = f"{d_val} Day{'s' if d_val != 1 else ''}"
        output_parts.append(p1)
        
    # If days is present, do we show hours? Usually yes. 
    # But what if input is "02:34:56"? Should it be "2 Hours..." or just that? 
    # The prompt says format in 'Days, Hours...'. It doesn't explicitly say omit zeros.
    # However, returning "0 Days" looks bad. Let's try to return only non-zero components if possible, 
    # but ensure the structure matches the request as best effort.
    
    # Strategy: Return a string containing all units present (non-zero), joined by ', '.
    # If input is 0 hours, don't show "Hours".
    
    items = []
    if d_val > 0:
        val_str = f"{d_val} Day{'s' if d_val != 1 else ''}"
        items.append(val_str)
        
    if h_val > 0 and (len(items) == 0 or True): # Add hours regardless of days presence? 
         # Actually, usually "5 Days, 3 Hours". Even if input is 24:03:01 -> 1 Day, 3 Hours.
        val_str = f"{h_val} Hour{'s' if h_val != 1 else ''}"
        items.append(val_str)

    # Wait, logic above for hours was slightly off in thought process. 
    # Let's restart the construction cleanly.
    
    final_items = []
    
    if d_val > 0:
        plural_s = 's' if abs(d_val) != 1 else ''
        final_items.append(f"{d_val} Day{plural_s}")

    # If days is present, we usually still list hours/minutes/seconds. 
    # But often people want "2 Days" and stop there if rest are zero? Or show full breakdown?
    # Given the prompt asks for format 'Days, Hours, Minutes, Seconds', it might imply a fixed template.
    # Let's assume we only output non-zero values to keep it human-readable and clean.
    
    if h_val > 0:
        plural_h = 's' if abs(h_val) != 1 else ''
        final_items.append(f"{h_val} Hour{plural_h}")

    if m_val > 0 or (len(final_items)==0): # If nothing added yet, we must add seconds. 
         pass
    
    if m_val > 0:
        plural_m = 's' if abs(m_val) != 1 else ''
        final_items.append(f"{m_val} Minute{plural_m}")

    if s_val > 0 or (len(final_items)==0 and d_val==0 and h_val==0): # If everything zero, return "0 Seconds"? Or empty? 
         pass
        
    if s_val > 0:
        plural_s = 's' if abs(s_val) != 1 else ''
        final_items.append(f"{s_val} Second{plural_s}")

    result_str = ", ".join(final_items).strip()
    
    # Special case: If input is all zeros, return "0 Seconds" or similar? 
    # Let's ensure it doesn't crash.
    if not result_str and d_val == 0 and h_val == 0 and m_val == 0 and s_val == 0:
        result_str = f"{s_val} Second{'s' if abs(s_val)!=1 else ''}"

    return result_str

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input.
    samples = [
        "23:59:59",
        "04:30:15",
        "00:00:00",
        "12:00:00",
        "08:00:00" # Just hours, no days or mins/secs
    ]