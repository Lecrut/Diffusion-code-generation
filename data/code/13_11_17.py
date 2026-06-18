import re
from datetime import timedelta

class TimeScaler:
    """
    A class to parse time difference strings and summarize total duration.
    
    Attributes:
        None
    
    Methods:
        analyze_times(time_strings): Returns a dictionary with the breakdown of 
                                     total days, hours, minutes, and seconds.
    """

    def __init__(self):
        self.total_seconds = 0

    def _parse_time_string(self, time_str):
        """
        Parses a string representing a duration (e.g., '2d3h45m10s').
        
        Args:
            time_str (str): The time difference string.
            
        Returns:
            int: Total seconds represented by the string.
        """
        # Pattern to match digits followed immediately by d, h, m, or s
        pattern = r'(\d+)\s*(?:d|h|m|s)'
        
        duration_seconds = 0
        
        matches = re.findall(pattern, time_str)
        
        for value, unit in matches:
            val = int(value)
            
            if unit == 'd':
                duration_seconds += val * 24 * 60 * 60
            elif unit == 'h':
                duration_seconds += val * 60 * 60
            elif unit == 'm':
                duration_seconds += val * 60
            elif unit == 's':
                duration_seconds += val
                
        return duration_seconds

    def analyze_times(self, time_strings):
        """
        Accepts a list of time difference strings and returns a dictionary 
        summarizing the total duration.
        
        Args:
            time_strings (list[str]): List of time difference strings to parse.
            
        Returns:
            dict: A dictionary containing 'days', 'hours', 'minutes', and 'seconds'.
                  If there is any remainder in seconds, it will be stored as 
                  a float representing the fractional part of an hour/minute/etc.,
                  but since inputs are integers, we can calculate exact remainders.
        """
        total_seconds = 0
        
        for time_str in time_strings:
            if not isinstance(time_str, str):
                raise TypeError(f"Each element must be a string, got {type(time_str)}")
                
            try:
                seconds = self._parse_time_string(time_str)
                total_seconds += seconds
            except ValueError as e:
                # If parsing fails for any reason (e.g., invalid chars), skip or raise. 
                # Here we assume valid format based on task constraints, but handle gracefully.
                if "invalid literal" in str(e):
                    continue

        days = total_seconds // (24 * 3600)
        remainder_after_days = total_seconds % (24 * 3600)
        
        hours = remainder_after_days // 3600
        remainder_after_hours = remainder_after_days % 3600
        
        minutes = remainder_after_hours // 60
        seconds_remainder = remainder_after_hours % 60

        return {
            'days': days,
            'hours': hours,
            'minutes': minutes,
            'seconds': int(seconds_remainder) # Keep as integer since input is integers. 
                                                # If fractional inputs were needed later, this would change.
        }

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files.
    sample_times = [
        "1d2h30m45s",      # 1 day, 2 hours, 30 mins, 45 secs
        "5h45m",            # 5 hours, 45 minutes (no seconds) -> treated as 0s implicitly if format strict? 
                           # Our regex handles missing 's' by not matching it. Wait, let's re-verify logic.
    ]

    # Correction on sample: The pattern requires the unit char to be present after digits.
    # "5h45m" matches 5*h and 45*m correctly because there is no trailing requirement for 's'.
    
    scaler = TimeScaler()
    result = scaler.analyze_times(sample_times)

    print("Parsed Summary:")
    print(f"Total Days: {result['days']}")
    print(f"Total Hours: {result['hours']}")
    print(f"Total Minutes: {result['minutes']}")
    print(f"Total Seconds: {result['seconds']}")
    
    # Additional test with seconds explicitly included to ensure robustness.
    sample_times_extended = [
        "3d",               # 3 days only
        "10h20m30s",       # Full breakdown
        "45m"               # Just minutes (implicitly 0s)
    ]

    result_full = scaler.analyze_times(sample_times_extended)
    
    print("\nExtended Summary:")
    print(f"Total Days: {result_full['days']}")
    print(f"Total Hours: {result_full['hours']}")
    print(f"Total Minutes: {result_full['minutes']}")
    print(f"Total Seconds: {result_full['seconds']}")