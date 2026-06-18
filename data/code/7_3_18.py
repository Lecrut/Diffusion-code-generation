import re

def format_duration(duration_str: str) -> str:
    """
    Converts a time duration string in 'HH:MM:SS' format 
    into a human-readable string 'Days, Hours, Minutes, Seconds'.
    
    Args:
        duration_str (str): Time duration as a string in 'HH:MM:SS' format.
        
    Returns:
        str: Human-readable time string with leading zeros for single-digit values.
             If the total seconds are less than 24 hours and no days exist, 
             it returns just Hours, Minutes, Seconds without Days component.
    
    Raises:
        ValueError: If input format is invalid or contains non-numeric characters.
    """
    pattern = r'^(\d{1,2}):(\d{2}):(\d{2})$'
    match = re.match(pattern, duration_str.strip())

    if not match:
        raise ValueError(f"Invalid time format '{duration_str}'. Expected 'HH:MM:SS'.")

    hours = int(match.group(1))
    minutes = int(match.group(2))
    seconds = int(match.group(3))

    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    
    days = total_seconds // 86400
    remaining_after_days = total_seconds % 86400
    hours_remaining = remaining_after_days // 3600
    minutes_remaining = (remaining_after_days % 3600) // 60
    seconds_final = remaining_after_days % 60

    if days > 0:
        return f"{days} Days, {hours_remaining:02d} Hours, {minutes_remaining:02d} Minutes, {seconds_final:02d} Seconds"
    
    else:
        # If no full day has passed but hours exist (e.g., 13:45:30)
        if hours > 0 or minutes > 0 or seconds > 0:
            return f"{hours_remaining:02d} Hours, {minutes_remaining:02d} Minutes, {seconds_final:02d} Seconds"
        
    # Edge case where input is exactly "00:00:00" -> returns empty string per logic above? 
    # Let's ensure at least something if all zero based on typical expectations or return 0s.
    # Re-evaluating requirement for 'HH:MM:SS' conversion usually implies showing components even if small.
    # If input is "00:00:00", the above logic returns empty string because days=0, hours=0... 
    # Let's adjust to show 0 Hours etc if all are zero or just follow strict output format for non-zero inputs?
    # Based on standard interpretation of such tasks, we should probably return "0 Days..." only if >24h.
    # But what about <1 day with hours>0? The spec says 'Days, Hours...'. If days is 0, omit it unless specified otherwise.
    # However to be safe and consistent for edge cases like 00:05:03 -> "05 Minutes..." or similar logic might apply but 
    # the prompt specifically asks for format string containing Days if applicable else skip?
    # Let's stick to strict interpretation: Only include 'Days' if days > 0. Otherwise omit it entirely from output structure unless all are zero?
    # Actually, looking at common implementations of this task (like `duration` library), 
    # often they show "5 minutes" for small durations without forcing a specific header like "Hours".
    # But the prompt says: convert to 'Days, Hours, Minutes, Seconds'. This implies all components might be expected if >0.
    # Let's refine logic: If total_seconds == 0 return empty or "0 Days..."? 
    # Given no explicit rule for zero input in prompt, let's assume standard behavior where we show what exists.
    
    # Refined Logic for <24h case to match 'Days, Hours...' structure if possible without leading zeros confusion:
    # If days == 0 and hours > 0 -> "X Hours..." 
    # If days == 0 and hours == 0 but minutes > 0 -> "Y Minutes..." etc.
    
    return f"{hours_remaining:02d} Hours, {minutes_remaining:02d} Minutes, {seconds_final:02d} Seconds"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    samples = [
        "13:45:30",   # Should output something like 13 Hours... since < 24h? Or maybe just show hours.
                     # Wait, if I have 1 day and some time -> Days included. If less than a day -> No days in string.
        "25:00:00",   # Should output 1 Day, ... 
        "00:05:30",   # Less than an hour? Just minutes/seconds or hours too (0)?
                     # Let's re-read prompt carefully: 'Days, Hours, Minutes, Seconds'.
                     # It does not say "only if > X". So maybe always include all with 0 padding for <1 day case?
    ]

    print("Sample Output:")
    for s in samples:
        try:
            result = format_duration(s)
            print(f"Input: {s} -> Output: '{result}'")
        except ValueError as e:
            print(f"Error processing '{s}': {e}")