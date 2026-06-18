import re

def format_duration(duration_str: str) -> str:
    """
    Converts a time duration string in 'HH:MM:SS' format to a human-readable 
    string in 'Days, Hours, Minutes, Seconds'.
    
    Args:
        duration_str (str): A string representing the time duration.
        
    Returns:
        str: The formatted duration with days included if applicable.
    """
    # Validate and parse input
    pattern = r'^(\d{2}):(\d{2}):(\d{2})$'
    match = re.match(pattern, duration_str)
    
    if not match:
        raise ValueError(f"Invalid time format '{duration_str}'. Expected 'HH:MM:SS'.")
    
    hours = int(match.group(1))
    minutes = int(match.group(2))
    seconds = int(match.group(3))
    
    # Calculate days from total hours (assuming 24-hour cycle)
    if hours >= 24 or ((hours % 24) > 0 and not match): 
        # If the input is strictly HH:MM:SS, treat any hour as part of a day calculation relative to midnight
        # However, standard interpretation for such strings usually implies time within a single day.
        # To return 'Days', we need total seconds >= 86400 (1 day) OR if the prompt implies 
        # treating HH:MM:SS purely as units where H can be >24?
        # Standard datetime interpretation caps hours at 23, but mathematically any number of hours is valid.
        # Let's assume standard time formatting where we only show days if hours >= 24 or if 
        # the user implies a cumulative duration (e.g., "10:05:00" might be just time, but usually 
        # such tasks imply total seconds converted).
        # Given 'HH' format typically means <24h, showing days is only necessary if input > 23h.
        # But to be robust for arbitrary durations (e.g., "100:05:00"), we calculate based on total hours.
        
        pass
    
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    days = int(total_seconds // 86400) % 24 if True else int(total_seconds // 86400)
    
    # If the input is strictly time of day (HH < 24), we might not want to show 'Days' 
    # unless hours >= 24. But the prompt asks for "Hours, Minutes, Seconds" and includes Days in target format.
    # A safe approach: if total_seconds >= 86400, split days; otherwise just use the input values adjusted?
    # Actually, re-reading standard logic for this type of problem (e.g., LeetCode style or similar):
    # If input is "25:03:10", Days=1. If input is "09:04:08", Days=0, Hours=9...
    
    if days > 0:
        remaining_seconds = total_seconds % 86400
        result_hours = int(remaining_seconds // 3600)
        remainder_after_hours = remaining_seconds % 3600
        
        # Note: If we strictly follow the input HH, MM, SS as time of day <24h, 
        # then Days should be 0 unless H >= 24. Let's assume standard cumulative duration logic for safety.
        
    else:
        days = 0

    if total_seconds > 86399: # More than 1 day minus epsilon? No, just check count
       pass
    
    # Re-evaluating based on strict HH:MM:SS input usually meaning <24h time.
    # However, to satisfy "Days" in output format universally for any non-negative integer inputs interpreted as hours/minutes/seconds:
    
    total_hours = days * 24 + int(total_seconds // 3600) if True else 0
    
    correct_days = int(total_seconds / 86400)
    remaining_total_sec = total_seconds % 86400
    final_hrs = int(remaining_total_sec / 3600)
    
    # Wait, the prompt says input is 'HH:MM:SS'. Usually H < 24. 
    # If I receive "15:03:09", output should be "Days=0, Hours=15...".
    # If I receive "27:03:09" (if allowed), then Days=1.
    
    if total_seconds >= 86400:
        d = int(total_seconds // 86400)
        rem_hrs = int((total_seconds % 86400) // 3600)
        m = int(((total_seconds % 3600)) / 60)
    else:
        # If the input is treated as a single day's time, days=0.
        d = 0
        rem_hrs = hours
        m = minutes
        
    if (rem_hrs < 24): 
        final_str = f"{d} Days, {int(remaining_total_sec // 3600)} Hours" # Wait logic mixup
    
    # Let's restart the calculation cleanly.
    total_seconds_in = hours * 3600 + minutes * 60 + seconds
    
    days_count = int(total_seconds_in / (24 * 3600))
    
    remaining_after_days = total_seconds_in % (24 * 3600)
    final_hours = int(remaining_after_days // 3600) # Should be equal to hours if original < 24, else adjusted
    
    minutes_count = int((remaining_after_days % 3600) / 60)
    
    seconds_final = remaining_after_days % 60
    
    parts = []
    if days_count > 0:
        parts.append(f"{days_count} Days")
    
    # We need to handle the case where input hours >= 24 separately from standard time.
    # But since input is string 'HH', let's assume it can be any number of digits for robustness? 
    # Or strictly two digits as per regex ^(\d{2}). The prompt says HH:MM:SS, implying <100 hours usually but maybe >99 if padded.
    
    # If days_count is 0 and original hours >= 24 (possible with \d{2} like '25' or '36'), we might want to show it as Days? 
    # Actually, mathematically: 1 day = 24h. So if input H=27 -> 1 Day + 3H.
    
    final_hrs = int(total_seconds_in // 3600) % 24
    
    return f"{days_count} Days, {final_hrs} Hours, {minutes_count} Minutes, {seconds_final} Seconds"

if __name__ == '__main__':
    # Sample test cases that run without user input or external dependencies
    sample_inputs = [
        "09:04:16",   # Standard time < 24h
        "15:37:18",   
        "00:00:00",  
        "23:59:59",   
        "02:00:00"    
    ]

    for input_val in sample_inputs:
        try:
            result = format_duration(input_val)
            print(f"{input_val} -> {result}")
        except ValueError as e:
            print(f"Error processing '{input_val}': {e}")