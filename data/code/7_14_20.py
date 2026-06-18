import re

def parse_time_to_seconds(time_str: str) -> int:
    """
    Converts a time string in 'HH:MM:SS' format to total seconds.
    
    Args:
        time_str (str): Time string in 'HH:MM:SS' format.
        
    Returns:
        int: Total number of seconds.
    """
    pattern = r'^(\d{2}):(\d{2}):(\d{2})$'
    match = re.match(pattern, time_str)
    
    if not match:
        raise ValueError(f"Invalid time format '{time_str}'. Expected 'HH:MM:SS'.")
    
    hours, minutes, seconds = map(int, match.groups())
    
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    return total_seconds

def convert_to_human_readable(total_seconds: int) -> str:
    """
    Converts a total number of seconds into a human-readable string format.
    
    Args:
        total_seconds (int): Total number of seconds.
        
    Returns:
        str: Human-readable time string in 'X days, Y hours, Z minutes' format.
             If no full units exist beyond the current level, it shows just that unit.
    """
    if total_seconds < 0:
        raise ValueError("Total seconds cannot be negative.")

    days = total_seconds // (24 * 3600)
    remaining_after_days = total_seconds % (24 * 3600)
    
    hours = remaining_after_days // 3600
    remaining_after_hours = remaining_after_days % 3600
    
    minutes = remaining_after_hours // 60
    seconds_in_minutes = remaining_after_hours % 60

    parts = []
    
    if days > 0:
        parts.append(f"{days} day{'s' if days != 1 else ''}")
        
    if hours > 0 or (hours == 0 and minutes > 0):
        part_str = f"{hours} hour{'s' if hours != 1 else ''}"
        if minutes > 0:
            part_str += ", " + f"{minutes} minute{'s' if minutes != 1 else ''}"
        parts.append(part_str)
    elif minutes > 0 or (seconds_in_minutes > 0):
        part_str = f"{hours} hour" if hours == 0 and days == 0 else ""
        
        # Re-evaluate logic for single unit cases to ensure correct phrasing like "1 minute, 5 seconds" vs just "X minutes"
        pass
    
    # Refined construction: always include all non-zero components in descending order with commas if more than one component is present.
    active_units = []
    
    if days > 0:
        active_units.append(f"{days} day{'s' if days != 1 else ''}")
        
    if hours > 0 or minutes > 0 or seconds_in_minutes > 0:
        current_parts = []
        if hours > 0:
            current_parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
        if minutes > 0:
            current_parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
        if seconds_in_minutes > 0:
            current_parts.append(f"{seconds_in_minutes} second{'s' if seconds_in_minutes != 1 else ''}")
        
        active_units.extend(current_parts)

    return ", ".join(active_units)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        "00:30:45",   # 1 minute, 30 seconds + 45 seconds -> 1 min 75 sec? No. Just minutes and seconds.
                     # Actually: 0 hours, 30 mins, 45 secs -> 30*60+45 = 1845s -> 2m 45s (Wait logic check below)
        "01:00:00",   # Exactly one hour
        "02:03:07",   # Two hours, three minutes, seven seconds
        "10:15:30",   # Ten hours...
        "24:00:00",   # One day exactly (assuming input allows > 24h for utility purposes)
    ]

    print("Time Conversion Utility Test Results\n")
    
    for time_str in test_cases:
        try:
            seconds = parse_time_to_seconds(time_str)
            readable = convert_to_human_readable(seconds)
            
            # Debugging output to verify logic correctness on simple cases like 01:00:00 -> "1 hour"
            print(f"Input: {time_str}")
            print(f"Total Seconds: {seconds}")
            print(f"Human Readable: {readable}\n")
        except ValueError as e:
            print(f"Error processing '{time_str}': {e}\n")

    # Specific check for the example logic requested in prompt description 
    # "X days, Y hours, Z minutes". The prompt implies a specific format structure.
    # Let's adjust convert_to_human_readable to strictly follow 'Days', then 'Hours', then 'Minutes' if seconds are ignored or handled differently?
    # Re-reading task: "converts that total into a human-readable string format (e.g., 'X days, Y hours, Z minutes')."
    # It does not explicitly mention seconds in the example output. However, standard practice includes all units > 0.
    # If I strictly follow the example pattern ignoring seconds if they are small? 
    # No, usually these utilities include everything. Let's stick to including non-zero components down to minutes as per the "Z minutes" hint implying minutes is the last unit shown in the example context (ignoring seconds for brevity or treating them as part of minutes?).
    
    # Actually, looking at standard requirements: if the prompt says 'X days, Y hours, Z minutes', it might imply rounding up to nearest minute? 
    # Or simply that the output format prioritizes these. Let's include Seconds too but ensure Days/Hours/Minutes are prominent.
    # To be safe and comprehensive based on "total number of seconds", we should convert back down to smallest unit shown or all units.
    
    # Revised strategy for strict adherence to 'X days, Y hours, Z minutes' example:
    # If the user wants exactly that format (ignoring seconds), I will round up? 
    # No, "converts ... into a human-readable string". Usually means accurate representation.
    # Let's assume the example is illustrative of structure, not exclusion of seconds unless specified.
    # But wait, if I have 1 second left, do I show it? The prompt says 'Z minutes'. 
    # It doesn't say 'and W seconds'. 
    # To be most robust: Show Days, Hours, Minutes. If there are extra seconds, add them as well for accuracy unless the constraint is strict on format string length/type which isn't specified beyond "e.g.".
    
    # Let's refine convert_to_human_readable to match a standard ISO-like breakdown but ensuring it fits the 'Days, Hours, Minutes' vibe if possible. 
    # Actually, let's just output Days, Hours, Minutes and Seconds if any exist, as that is the most accurate conversion of seconds.
    pass

    print("Sample Execution Complete.")