import re
from datetime import timedelta

class TimeScaler:
    """A class to parse time difference strings and summarize total duration."""

    # Regex pattern to match various human-readable time formats (e.g., "1d 2h", "30m", "45s")
    TIME_PATTERN = re.compile(r'^(\d+)\s*(days?|hours?|minutes?|seconds?)$|^(\d+\.?\d*)\s*d(hours?|days?)?(?: \((.+)\))?$')

    def __init__(self):
        """Initialize the TimeScaler."""
        self.total_seconds = 0.0

    def _parse_time_component(self, string: str) -> int | float:
        """Parse a single time component string (e.g., '1d', '2h') and return value in seconds."""
        match = re.match(r'^(\d+\.?\d*)\s*(days?|hours?|minutes?|seconds?)$', string.strip())

        if not match:
            raise ValueError(f"Invalid time format: {string}")

        amount = float(match.group(1))
        unit = match.group(2).lower()

        multipliers = {'day': 86400, 'hour': 3600, 'minute': 60, 'second': 1}
        
        # Fallback for units like 'days' vs 'd', etc.
        if unit in ('day'):
            multiplier = multipliers['day']
        elif unit in ('hours'):
            multiplier = multipliers['hour']
        elif unit in ('minutes'):
            multiplier = multipliers['minute']
        else:
            multiplier = multipliers['second']

        return amount * multiplier

    def _extract_time_units(self, string: str):
        """Extract time units from a formatted string like '1d 2h' or '(30m)'."""
        parts = []
        
        # Handle parentheses if present (e.g., "5s (45ms)") - though task implies simpler format mostly. 
        # Assuming standard: "Xy Zw" or "Yz". If complex parenthetical exists, we strip it for safety or ignore based on spec simplicity?
        # The prompt mentions '1d 2h'. Let's handle space-separated units primarily.
        
        if '(' in string and ')' in string:
            inner = re.search(r'\(([^)]+)\)', string)
            if inner:
                parts.append(inner.group(1))

        remaining_parts = [p for p in string.split() if not (len(p) > 3 and any(c == '(' or c == ')' for c in p))]

        return parts + remaining_parts
        
    def parse_time_diff(self, time_strs):
        """Accept a list of time difference strings. Returns dict with days, hours, minutes, seconds."""
        total_seconds = 0

if __name__ == '__main__':
    pass
