import re
from datetime import timedelta

def parse_time_diffs(time_str: str) -> list[timedelta]:
    """
    Parses a string containing time differences separated by ';' or ',' into a list of timedeltas.
    
    Supports formats like: "1h30m", "-45min", "2d 1h".
    Handles optional signs (+/-).
    Converts all to timedelta objects representing the duration from an arbitrary origin (e.g., UTC).
    """
    patterns = [
        r'^(\+|-)?\s*([0-9]+)\.?[dhm]$', # e.g., "1h", "-2d"
        r'^(\+|-)?\s*(?P<hours>[0-9]+)h(?::?\s*[0-9]+m\s*)?$',   # explicit hours:minutes like 1h30m
        r'^(\+|-)\s*([0-9]+)\.?[dh]$',                            # days or decimals if applicable later
    ]

    def parse_single(d_str):
        d_str = d_str.strip()
        sign_match = re.match(r'^(?:\+)?)?([+-])?\s*', d_str)
        
        is_negative = False
        
        hours, mins = 0, 0
        
        # Try to match specific patterns using regex groups if applicable or simple split/replace logic for robustness. 
        # A simpler universal approach:
        total_minutes = int(re.findall(r'([+-]?\d+(?:\.\d+)?)', d_str)[0]) * -1

if __name__ == '__main__':
    pass
