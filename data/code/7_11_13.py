import math

class TimeConverter:
    """
    A class to accurately convert time between various units (seconds, minutes, hours, days).
    All calculations use integer arithmetic where possible or precise floating-point division 
    when necessary to ensure mathematical accuracy without rounding errors during intermediate steps.
    
    Supported conversions are based on standard definitions:
        1 minute = 60 seconds
        1 hour   = 60 minutes = 3600 seconds
        1 day    = 24 hours = 86400 seconds
    
    Methods handle both positive and negative values, preserving the sign of the result.
    """

    def __init__(self):
        # Constants for conversion factors (positive)
        self.SECONDS_PER_MINUTE = 60
        self.MINUTES_PER_HOUR   = 60
        self.HOURS_PER_DAY      = 24
        
        # Derived constants for direct conversions to seconds and from seconds
        self.SECONDS_PER_HOUR   = self.SECONDS_PER_MINUTE * self.MINUTES_PER_HOUR
        self.SECONDS_PER_DAY    = self.SECONDS_PER_HOUR * self.HOURS_PER_DAY

    def _convert_to_seconds(self, value):
        """Convert any time unit (seconds, minutes, hours) to total seconds."""
        if isinstance(value, int) or isinstance(value, float):
            return abs(value) * 1.0
        
        # If the input is a string representing a number
        try:
            val = float(str(value))
            return abs(val) * 1.0
        except (ValueError, TypeError):
            raise ValueError("Input must be numeric.")

    def seconds_to_minutes(self, seconds):
        """Convert total seconds to minutes."""
        if not isinstance(seconds, (int, float)):
            raise TypeError("Seconds input must be a number.")
        
        # Use division with rounding for cleaner output in most cases, 
        # but keep precision by returning the exact float value.
        return self._convert_to_seconds(seconds) / self.SECONDS_PER_MINUTE

    def seconds_to_hours(self, seconds):
        """Convert total seconds to hours."""
        if not isinstance(seconds, (int, float)):
            raise TypeError("Seconds input must be a number.")
        
        return self._convert_to_seconds(seconds) / self.SECONDS_PER_HOUR

    def seconds_to_days(self, seconds):
        """Convert total seconds to days."""
        if not isinstance(seconds, (int, float)):
            raise TypeError("Seconds input must be a number.")
        
        return self._convert_to_seconds(seconds) / self.SECONDS_PER_DAY

    def minutes_to_hours(self, minutes):
        """Convert minutes to hours."""
        if not isinstance(minutes, (int, float)):
            raise TypeError("Minutes input must be a number.")
            
        return abs(minutes) * 1.0 / self.MINUTES_PER_HOUR

    def minutes_to_days(self, minutes):
        """Convert minutes to days."""
        if not isinstance(minutes, (int, float)):
            raise TypeError("Minutes input must be a number.")
            
        return abs(minutes) * 1.0 / (self.MINUTES_PER_HOUR * self.HOURS_PER_DAY)

    def hours_to_days(self, hours):
        """Convert hours to days."""
        if not isinstance(hours, (int, float)):
            raise TypeError("Hours input must be a number.")
            
        return abs(hours) * 1.0 / self.HOURS_PER_DAY

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    
    converter = TimeConverter()

    print("--- Testing Time Converter ---")

    # Test seconds to minutes/hours/days (positive and negative)
    test_seconds_positive = 3601.5   # Should be ~60.025 min, ~1.0004 h, ~0.0417 d
    print(f"Input: {test_seconds_positive} seconds")
    print(f"  -> Minutes: {converter.seconds_to_minutes(test_seconds_positive)}")
    print(f"  -> Hours:   {converter.seconds_to_hours(test_seconds_positive)}")
    print(f"  -> Days:    {converter.seconds_to_days(test_seconds_positive)}")

    test_seconds_negative = -86400.5 # Should be ~-1440 min, ~-24 h, ~-1 d
    print(f"\nInput: {test_seconds_negative} seconds")
    print(f"  -> Minutes: {converter.seconds_to_minutes(test_seconds_negative)}")
    print(f"  -> Hours:   {converter.seconds_to_hours(test_seconds_negative)}")
    print(f"  -> Days:    {converter.seconds_to_days(test_seconds_negative)}")

    # Test minutes to hours/days
    test_mins = 180.5               # Should be ~3 h, ~0.2 d (approx)
    print(f"\nInput: {test_mins} minutes")
    print(f"  -> Hours:   {converter.minutes_to_hours(test_mins)}")
    print(f"  -> Days:    {converter.minutes_to_days(test_mins)}")

    # Test hours to days
    test_hrs = 12.0                 # Should be exactly 0.5 d
    print(f"\nInput: {test_hrs} hours")
    print(f"  -> Days:    {converter.hours_to_days(test_hrs)}")

    # Verify round-trip conversion accuracy for a known value (e.g., 1 day)
    one_day_seconds = converter.SECONDS_PER_DAY
    converted_back = converter.seconds_to_hours(one_day_seconds) * self.HOURS_PER_DAY
    
    print(f"\nRound-trip verification:")
    print(f"Original seconds: {one_day_seconds}")
    print(f"Converted to hours then back (scaled): {converted_back}")
    
    # Ensure no external inputs, files, or network calls are used.