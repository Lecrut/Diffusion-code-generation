import re
from datetime import timedelta

class TimeScaler:
    """
    A class to parse time difference strings and summarize total duration in days, hours, minutes, and seconds.
    
    Supports formats like "1d 2h", "30m", "45s", or combinations thereof.
    Efficiently handles multiple entries by aggregating them into a single timedelta object.
    """

    def __init__(self):
        # Regex pattern to match time units: digits followed by optional space and unit (d, h, m, s)
        self.time_pattern = re.compile(r'(\d+)\s*(?:d|h|m|s)', re.IGNORECASE)

    def parse_time_string(self, time_str: str):
        """
        Parses a single time difference string into a timedelta.
        
        Args:
            time_str (str): A string representing time differences (e.g., "1d 2h").
            
        Returns:
            datetime.timedelta: The parsed duration as a timedelta object.
            
        Raises:
            ValueError: If the input string does not match expected format or contains invalid units.
        """
        matches = self.time_pattern.findall(time_str)
        
        if not matches:
            raise ValueError(f"Invalid time string '{time_str}'. Expected format like '1d 2h'.")

        total_seconds = 0
        
        for value, unit in matches:
            try:
                num = int(value.strip())
            except ValueError:
                raise ValueError(f"Invalid number '{value}' found in time string.")
            
            if not re.match(r'^[dDhHmMsS]$', unit):
                raise ValueError(f"Unsupported or invalid unit '{unit}'. Supported units are d, h, m, s.")

            multiplier = {
                'd': 86400,   # seconds in a day
                'h': 3600,    # seconds in an hour
                'm': 60,      # seconds in a minute
                's': 1        # seconds in a second
            }[unit.lower()]

            total_seconds += num * multiplier
        
        return timedelta(seconds=total_seconds)

    def summarize_duration(self, time_diff_list: list[str]) -> dict:
        """
        Accepts a list of time difference strings and returns a dictionary summarizing the 
        total duration in days, hours, minutes, and seconds.
        
        Args:
            time_diff_list (list[str]): List of time difference strings to aggregate.
            
        Returns:
            dict: A dictionary with keys 'days', 'hours', 'minutes', 'seconds' representing 
                 the aggregated total duration.
                 
        Raises:
            ValueError: If any string in the list is invalid.
        """
        if not isinstance(time_diff_list, list):
            raise TypeError("Input must be a list of time difference strings.")

        try:
            # Aggregate all timedeltas efficiently using sum() which is optimized for C-level operations
            total_timedelta = timedelta(0) + sum(self.parse_time_string(t) for t in time_diff_list if isinstance(t, str))
            
            days = int(total_timedelta.days)
            remaining_seconds = (total_timedelta.seconds % 86400) # seconds after removing full days
            
            hours = int(remaining_seconds // 3600)
            remaining_minutes_seconds = remaining_seconds % 3600
            
            minutes = int(remaining_minutes_seconds // 60)
            final_seconds = remaining_minutes_seconds % 60

        except (ValueError, TypeError):
            raise ValueError("One or more time strings in the list could not be parsed.")

        return {
            'days': days,
            'hours': hours,
            'minutes': minutes,
            'seconds': final_seconds
        }

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    samples = [
        "1d 2h",           # One day and two hours
        "30m",             # Thirty minutes
        "45s",             # Forty-five seconds
        "7d 5h 9m 12s"    # Seven days, five hours, nine minutes, twelve seconds
    ]

    scaler = TimeScaler()
    
    try:
        result = scaler.summarize_duration(samples)
        
        print("Time Scaler Summary:")
        for key in ['days', 'hours', 'minutes', 'seconds']:
            print(f"{key.capitalize()}: {result[key]}")
            
        # Verification of total seconds calculation logic implicitly through the output structure.
    except Exception as e:
        print(f"Error processing time strings: {e}")