import re
from datetime import datetime

def parse_time_diffs(time_string: str) -> list[datetime]:
    """
    Parses a string containing time differences separated by ';' 
    or other common delimiters, and returns a list of datetime objects.
    
    Assumes the input format is relative to '00:00:00' (midnight).
    Example inputs: "1h30m", "+45min", "-2d", "P1D" (ISO 8601 duration)
    """
    # Regex pattern to match various time formats including ISO 8601 durations and simple HH:mm:ss or H:M:S with optional +/- sign
    # Matches: 
    #   - Optional +/minus followed by number of days, hours, minutes, seconds (e.g., P1D, 2h30m)
    #   - Simple time format like "14:30" interpreted as offset from midnight if no 'd' or specific unit markers are clear without context. 
    #     However, to be robust for "time differences", we primarily look for duration-like strings (e.g., 2h, +5min).
    #   - If the string looks like a clock time (HH:MM), it's ambiguous as a difference unless specified relative to midnight. 
    #     Given the task says "time differences", we assume inputs are durations or ISO 8601 duration strings if possible.
    
    # Let's support explicit units: d, h, m, s with optional +/- and P (ISO).
    pattern = r'^([+-]?\d+)?\s*(P(?:[^\dT]*T\d+(?::\d+(?:,\d+)*)?)?(?:[\dT]\d{2}(?::\d+(?:,\d+)*)?)?(?:W\d+)?|\S+)\s*([dhmsDHDHMD])$'
    
    # Actually, let's simplify for maximum compatibility with common duration strings while avoiding complex regex failures.
    # We will split by ';' or ',' and try to parse each token as a timedelta-like string.
    tokens = re.split(r'[;,]', time_string.strip())
    times = []

    for t in tokens:
        if not t:
            continue
        
        # Try parsing ISO 8601 duration first (e.g., P1D, PT3H45M) or simple H:M:S with units attached like "2h"
        
        # Remove surrounding whitespace
        token = t.strip()
        if not token:
            continue

if __name__ == '__main__':
    pass
