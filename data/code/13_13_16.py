import re
from datetime import datetime

def parse_time_diffs(time_str):
    """
    Parses a string containing time differences separated by ';' 
    and returns a list of (start, end) tuples representing absolute times.
    
    Assumption: The input format is 'HH:MM' for each segment.
    If the logic requires relative deltas to be converted to absolute,
    we assume an arbitrary start point or that the segments are already 
    full time points if they look like HH:MM. Given the task asks for 
    "earliest and latest time points", it implies parsing timestamps directly.
    
    However, often such tasks imply a sequence of events where each segment
    might be 'start:end' relative to some base or just absolute times.
    Let's assume the input segments are individual HH:MM strings representing
    specific moments in time (e.g., "09:30;14:25"). If they were deltas, 
    calculating a net difference between earliest and latest would require an anchor.
    Since no anchor is provided, we treat each segment as an absolute timestamp relative to midnight.

    Args:
        time_str (str): A string like "HH:MM;HH:MM" or similar format separated by ';'.
    
    Returns:
        List[Tuple[int, int]]: Parsed times in seconds since epoch of day for calculation purposes 
                               (or just minutes from midnight). We'll use total_seconds_from_midnight.
    """
    # Regex to match time strings like HH:MM or H:M
    pattern = r'(\d{1,2}):(\d{2})|(\d{1,2}:\d{2}' + r'\s*[-+]?|\s*[+-]?\d+\s*\d+' 
              # Note: The prompt says "time differences" but asks for earliest/latest time points.
              # This usually implies a list of timestamps. If the input was strictly deltas like "+1h",
              # we couldn't find an 'earliest' without a start point. 
              # Therefore, we assume the segments are absolute times in HH:MM format separated by ';'.

if __name__ == '__main__':
    pass
