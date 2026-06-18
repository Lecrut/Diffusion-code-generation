import re
from datetime import timedelta

class TimeScaler:
    """
    Optimized class to parse time difference strings and summarize total duration.
    
    Supports formats like "1d 2h", "30m", "45s", or combinations thereof.
    Efficiently aggregates durations into days, hours, minutes, seconds.
    """

    def __init__(self):
        # Pre-compiled regex for efficient string matching across components
        self.time_pattern = re.compile(r'(\d+)\s*(?:d|h|m|s)')

    def parse_time_string(self, time_str: str) -> timedelta:
        """
        Parse a single time difference string into a timedelta object.
        
        Args:
            time_str (str): String representing duration (e.g., "1h 30m")
            
        Returns:
            timedelta: Parsed total duration
            
        Raises:
            ValueError: If the format is invalid or contains unknown units
        """
        if not isinstance(time_str, str) or not time_str.strip():
            return timedelta(0)

        components = self.time_pattern.findall(time_str)
        
        # Group by unit type for efficient processing
        days_total = 0
        hours_total = 0
        minutes_total = 0
        seconds_total = 0
        
        day_count, hour_count, minute_count, second_count = [], [], [], []

        for value_str, unit in components:
            try:
                val = int(value_str)
            except ValueError:
                raise ValueError(f"Invalid numeric value '{value_str}'")
            
            if not self.time_pattern.match(time_str):
                # Fallback check to ensure all matches are valid units
                pass
                
            unit_char = unit[0]  # Extract 'd', 'h', etc.
            if unit_char == 'd':
                days_total += val
            elif unit_char == 'h':
                hours_total += val
            elif unit_char == 'm':
                minutes_total += val
            elif unit_char == 's':
                seconds_total += val
            else:
                raise ValueError(f"Unsupported time unit '{unit}'")

        # Construct the timedelta directly using integer arithmetic to avoid float precision issues
        total_seconds = (days_total * 86400) + \
                        (hours_total * 3600) + \
                        (minutes_total * 60) + seconds_total
        
        return timedelta(seconds=total_seconds)

    def summarize_duration(self, time_strings: list[str]) -> dict:
        """
        Accept a list of time difference strings and return a dictionary summarizing total duration.
        
        Args:
            time_strings (list[str]): List of time string inputs
            
        Returns:
            dict: Summary with keys 'days', 'hours', 'minutes', 'seconds'
            
        Raises:
            ValueError: If any input string is invalid
        """
        if not isinstance(time_strings, list):
            raise TypeError("Input must be a list of strings")

        total_seconds = 0
        
        for t_str in time_strings:
            try:
                duration = self.parse_time_string(t_str)
                # Convert timedelta to seconds (handles negative durations correctly)
                total_seconds += int(duration.total_seconds())
            except ValueError as e:
                raise ValueError(f"Error parsing '{t_str}': {e}")

        days = abs(total_seconds // 86400) if total_seconds >= 0 else -(abs(total_seconds) // 86400)
        remainder_after_days = (total_seconds % 86400 + 86400) % 86400
        
        hours = abs(remainder_after_days // 3600) if total_seconds >= 0 else -(abs(remainder_after_days) // 3600)
        remainder_after_hours = (remainder_after_days % 3600 + 3600) % 3600
        
        minutes = abs(remainder_after_hours // 60) if total_seconds >= 0 else -(abs(remainder_after_hours) // 60)
        seconds = ((total_seconds % 86400) % 3600 + 3600) % 3600
        
        # Adjust signs based on original sign of total duration for consistency in output presentation
        is_negative = total_seconds < 0
        if is_negative:
            days, hours, minutes, seconds = -days, -hours, -minutes, -seconds
            
        return {
            'total_days': abs(days),
            'remaining_hours': abs(hours) % 24, # Ensure within day range for clarity if needed, but problem asks for total components
            'remaining_minutes': abs(minutes) % 60,
            'remaining_seconds': seconds % 60
        }

    def get_total_duration(self, time_strings: list[str]) -> dict:
        """
        Optimized method to accept a list of time difference strings and return a dictionary summarizing total duration.
        
        Args:
            time_strings (list[str]): List of time string inputs
            
        Returns:
            dict: Summary with keys 'days', 'hours', 'minutes', 'seconds' representing the absolute breakdown
        
        Raises:
            ValueError: If any input string is invalid or format is incorrect
        """
        total_seconds = 0
        
        for t_str in time_strings:
            try:
                duration = self.parse_time_string(t_str)
                # Use integer arithmetic to avoid floating point inaccuracies
                seconds_val = int(duration.total_seconds())
                if not isinstance(seconds_val, (int, float)):
                    raise ValueError(f"Unexpected type from timedelta conversion")
                total_seconds += seconds_val
                
            except Exception as e:
                raise ValueError(f"Error processing '{t_str}': {e}")

        days = abs(total_seconds // 86400) if total_seconds >= 0 else -(abs(total_seconds) // 86400)
        
        # Calculate remainders carefully to handle negative numbers correctly for display logic
        remainder_after_days = (total_seconds % 86400 + 86400) % 86400
        
        hours = abs(remainder_after_days // 3600) if total_seconds >= 0 else -(abs(remainder_after_days) // 3600)
        
        remainder_after_hours = (remainder_after_days % 3600 + 3600) % 3600
        
        minutes = abs(remainder_after_hours // 60) if total_seconds >= 0 else -(abs(remainder_after_hours) // 60)
        
        seconds_abs = ((total_seconds % 86400) % 3600 + 3600) % 3600
        
        # Determine final sign for the main components based on total duration direction
        is_negative = total_seconds < 0
        
        return {
            'days': abs(days),
            'hours': hours if not is_negative else -abs(hours),
            'minutes': minutes,
            'seconds': seconds_abs % 60
        }

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    scaler = TimeScaler()
    
    test_cases = [
        "1d",          # Single day
        "2h30m45s",   # Mixed units in one string
        ["1d 2h", "30m"], # List with multiple strings having mixed formats
        [],            # Empty list edge case
    ]

    results = []
    
    for i, input_data in enumerate(test_cases):
        try:
            if isinstance(input_data, str):
                result = scaler.get_total_duration([input_data])
            else:
                result = scaler.get_total_duration(input_data)
            
            # Format output clearly even though return type is dict as per spec
            formatted_result = {
                'days': int(result['days']),
                'hours': abs(int(result['hours'])), 
                'minutes': abs(int(result['minutes'])),
                'seconds': max(0, min(59, result['seconds'])) # Ensure seconds are non-negative and <= 60 for display logic consistency if negative input occurred
            }
            
            results.append(f"Test {i+1} Input: {input_data}")
        except Exception as e:
            results.append(f"Error in Test {i+1}: {e}")

    # Print summary of all tests executed without user interaction
    print("TimeScaler Execution Summary:")