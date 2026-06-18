import re
from datetime import timedelta

class TimeScaler:
    """
    A class to parse time difference strings and summarize total duration.
    
    Supports formats like "1d 2h", "30m", "45s", or combinations thereof.
    Efficiently aggregates durations into a dictionary with keys 'days', 'hours', 
    'minutes', and 'seconds'.
    """

    def __init__(self):
        self.total_seconds = timedelta(0)

    def parse_time_string(self, time_str: str) -> None:
        """
        Parses a single time difference string and adds to total duration.
        
        Args:
            time_str (str): A string representing time differences 
                           e.g., "1d 2h", "30m", "45s".
        """
        # Regex pattern to match components like 'Xd', 'Xh', 'Xm', 'Xs'
        pattern = r'^(\d+(?:\.\d+)?)\s*(d|h|m|s)$|^(\d+(?:\.\d+)?)\s*(d|h|m|s)\s*$'
        
        # More robust regex to capture number and unit, allowing optional spaces around units
        match = re.match(r'^([\d.]+)\s*([dhms])$', time_str.strip())
        
        if not match:
            raise ValueError(f"Invalid time string format: {time_str}")

        value = float(match.group(1))
        unit = match.group(2)

        # Convert to seconds and add to total
        multipliers = {'d': 86400, 'h': 3600, 'm': 60, 's': 1}
        
        self.total_seconds += timedelta(seconds=value * multipliers[unit])

    def get_summary(self) -> dict:
        """
        Returns a dictionary summarizing the total duration in days, hours, 
        minutes, and seconds.
        
        Returns:
            dict: Keys 'days', 'hours', 'minutes', 'seconds' with integer values.
                  Note: Since timedelta handles fractional seconds internally,
                  we convert back to integers for simplicity as per typical 
                  time difference summaries unless high precision is required.
        """
        days = self.total_seconds.days
        remaining = self.total_seconds - timedelta(days=days)
        
        hours = int(remaining.seconds // 3600)
        minutes = (remaining.seconds % 3600) // 60
        seconds = remaining.seconds % 60
        
        return {
            'days': days,
            'hours': hours,
            'minutes': minutes,
            'seconds': int(seconds)
        }

if __name__ == '__main__':
    # Hard-coded sample values to test the class functionality.
    samples = [
        "1d 2h",           # One day and two hours
        "30m",             # Thirty minutes
        "45s",             # Forty-five seconds
        "7d 5h 9m",        # Seven days, five hours, nine minutes
        "0.5d"             # Half a day (12 hours)
    ]

    scaler = TimeScaler()

    for sample in samples:
        try:
            scaler.parse_time_string(sample)
        except ValueError as e:
            print(f"Error parsing '{sample}': {e}")
    
    summary = scaler.get_summary()
    print("Total Duration Summary:")
    for key, value in summary.items():
        print(f"{key}: {value}")