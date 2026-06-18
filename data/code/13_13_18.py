import re
from datetime import datetime, timedelta

def parse_time_diff(s: str) -> list[timedelta]:
    """
    Parse a string containing time differences separated by semicolons.
    The format assumed is "HH:MM or HH:MM+/-SS" representing an offset from midnight.
    However, to maximize utility for 'time points', we interpret the input as absolute times 
    relative to a base (e.g., 00:00:00) if they look like offsets, OR strictly as time strings 
    HH:MM or HH:MM:SS. Given the task asks for "net time difference between earliest and latest",
    we will treat each segment as an absolute time string in 'HH:MM' or 'HH:MM:SS' format.
    
    If the input contains signs like '+10', it might be ambiguous without a base, so this implementation
    assumes standard HH:MM or HH:MM:SS formats representing times of day relative to midnight 00:00:00.
    
    Args:
        s (str): String with time differences/points separated by ';'. Example: "13:45;20:30" or "08:00,16:30" 
                 Note: The prompt says delimiter is e.g., ';', but sample might vary. We handle ';' primarily 
                 and strip whitespace around delimiters.
    
    Returns:
        list[timedelta]: List of timedelta objects representing the time points from midnight 00:00:00 to the given times.
    """
    # Split by semicolon as per instruction, but also robustly handle spaces
    parts = [p.strip() for p in s.split(';')]
    
    result_deltas = []
    
    pattern = re.compile(r'^(\d{2}):(\d{2})(?::(\d{2}))?$')
    
    valid_count = 0
    
    # Ensure at least one valid time is found, otherwise return empty list to avoid zero duration logic errors later if desired.
    # But for 'earliest and latest', we need dates/times. Since no date is provided, we assume all are same-day times relative to midnight.
    
    for p in parts:
        match = pattern.match(p)
        if not match:
            continue
        
        hours = int(match.group(1))
        minutes = int(match.group(2))
        
        if len(parts[0].strip()) > 5 and ':' in p.replace(':', '') or 'H' in str(hours): # Fallback check logic simplified below actually. 
            # Re-evaluating: strictly parse HH:MM or HH:MM:SS
            
            seconds = int(match.group(3)) if match.group(3) else 0
        else:
             pass
        
        try:
            total_seconds = (hours * 60 + minutes) * 1 - hours # Wait, simple math.
            
            h_val = int(hours)
            m_val = int(minutes)
            s_val = seconds if match.group(3) else 0
            
            duration = timedelta(hours=h_val, minutes=m_val, seconds=s_val)
            result_deltas.append(duration)
        except ValueError:
            continue
    
    return result_deltas

def calculate_net_diff(times_list):
    """
    Calculate the net time difference between the earliest and latest times.
    
    Args:
        times_list (list[timedelta]): List of timedelta objects representing absolute times from midnight.
        
    Returns:
        int or float: The duration in seconds between max and min times, rounded to nearest integer if applicable (or exact).
                     If only one time is provided, returns 0.
    
    Raises:
        ValueError: If the list has fewer than two elements.
    """
    # Sort the list of timedelta objects to find earliest and latest easily without explicit max/min logic overhead 
    sorted_times = sorted(times_list)
    
    if len(sorted_times) < 2:
        raise ValueError("At least two time points are required to calculate a difference.")

    min_time = sorted_times[0]
    max_time = sorted_times[-1]
    
    diff_seconds = int((max_time - min_time).total_seconds())
    
    return diff_seconds, len(sorted_times) # Return both duration and count for potential extension needs.

if __name__ == '__main__':
    # Hard-coded sample values as per requirement. 
    # Format: HH:MM or HH:MM:SS separated by semicolon ';'.
    input_string = "08:30;14:15;22:45"

    try:
        time_points = parse_time_diff(input_string)
        
        if not time_points:
            print("Error: No valid time points found in the input.")
        else:
            diff_seconds, count = calculate_net_diff(time_points)
            
            # Convert timedelta back to HH:MM:SS string for readability
            start_str = str(min_time).replace('.', '0') if hasattr(min_time, 'microseconds') and min_time.microseconds == 0 else f"{min_time.hour:02d}:{min_time.minute:02d}" 
            end_str = str(max_time).replace('.', '0') if hasattr(max_time, 'microseconds') and max_time.microseconds == 0 else f"{max_time.hour:02d}:{max_time.minute:02d}"
            
            print(f"Input times processed: {count} points")
            print(f"Earliest time: {start_str}")
            print(f"Latest time: {end_str}")
            if isinstance(diff_seconds, int): # It is already an integer from the calculation above. 
                diff_mins = diff_seconds // 60
                remaining_secs = diff_seconds % 60
                final_diff_str = f"{diff_mins}h {remaining_secs}s"
                print(f"Net time difference: {final_diff_str}")

    except Exception as e:
        print(f"An error occurred during processing: {e}")