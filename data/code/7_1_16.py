import math

class TimeConverter:
    """A class to convert between hours, minutes, and seconds efficiently."""

    def __init__(self):
        pass

    def total_seconds(self, hours=0, minutes=0, seconds=0) -> float:
        """Convert given time components into a single value in seconds.
        
        Args:
            hours (int or float): Number of hours.
            minutes (int or float): Number of minutes.
            seconds (float): Number of seconds.
            
        Returns:
            float: Total time in seconds.
        """
        return hours * 3600 + minutes * 60 + seconds

    def total_minutes(self, hours=0, minutes=0, seconds=0) -> float:
        """Convert given time components into a single value in minutes.
        
        Args:
            hours (int or float): Number of hours.
            minutes (int or float): Number of minutes.
            seconds (float): Number of seconds.
            
        Returns:
            float: Total time in minutes.
        """
        return self.total_seconds(hours, minutes, seconds) / 60

    def total_hours(self, hours=0, minutes=0, seconds=0) -> float:
        """Convert given time components into a single value in hours.
        
        Args:
            hours (int or float): Number of hours.
            minutes (int or float): Number of minutes.
            seconds (float): Number of seconds.
            
        Returns:
            float: Total time in hours.
        """
        return self.total_seconds(hours, minutes, seconds) / 3600

    def format_time(self, total_seconds=None, hours=0, minutes=0, seconds=0) -> str:
        """Format a duration into a human-readable string 'H:M:S'.
        
        Args:
            total_seconds (float): Optional. Total time in seconds to use for formatting.
            hours (int or float): Number of hours. Defaults to 0 if not provided with total_seconds.
            minutes (int or float): Number of minutes. Defaults to 0 if not provided with total_seconds.
            seconds (float): Number of seconds. Defaults to 0 if not provided with total_seconds.
            
        Returns:
            str: Formatted time string in 'H:M:S' format, zero-padded for single digits.
        """
        if total_seconds is None and hours == 0 and minutes == 0 and seconds == 0:
            raise ValueError("At least one of total_seconds or (hours, minutes, seconds) must be provided.")

        h = int(math.floor(total_seconds / 3600)) if total_seconds else hours
        m = int(math.floor((total_seconds % 3600) / 60)) if total_seconds else minutes
        s = round(total_seconds % 60, 2) if total_seconds else seconds

        return f"{h:0>2}:{m:0>2}:{s:.2f}"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    
    converter = TimeConverter()

    # Sample 1: Convert specific components to total seconds
    h, m, s = 3, 45, 30
    result_s = converter.total_seconds(h, m, s)
    print(f"Input (h={h}, m={m}, s={s}) -> Total Seconds: {result_s}")

    # Sample 2: Convert total seconds back to components and format string
    input_str = "1.5 hours, 30 minutes, 45 seconds"
    h_in, m_in, s_in = 1.5, 30, 45
    formatted_time = converter.format_time(hours=h_in, minutes=m_in, seconds=s_in)
    print(f"Input (h={h_in}, m={m_in}, s={s_in}) -> Formatted Time: {formatted_time}")

    # Sample 3: Convert total hours to other units
    h_total = 2.75
    result_mins = converter.total_minutes(hours=h_total)
    result_secs = converter.total_seconds(hours=h_total)
    print(f"Input (h={h_total}) -> Total Minutes: {result_mins}, Total Seconds: {result_secs}")

    # Sample 4: Verify mathematical soundness with edge case of zero input
    h_zero, m_zero, s_zero = 0, 0, 0
    result_s_zero = converter.total_seconds(h_zero, m_zero, s_zero)
    print(f"Input (h={h_zero}, m={m_zero}, s={s_zero}) -> Total Seconds: {result_s_zero}")

    # Sample 5: Large values to ensure no overflow issues in standard Python floats
    h_large = 1000
    result_s_large = converter.total_seconds(hours=h_large)
    print(f"Input (h={h_large}) -> Total Seconds: {result_s_large}")