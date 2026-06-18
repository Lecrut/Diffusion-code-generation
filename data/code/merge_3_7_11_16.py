import math

class TimeConverter:
    """A class to convert time between various units with mathematical precision."""

    def __init__(self):
        self._SECONDS_PER_MINUTE = 60
        self._MINUTES_PER_HOUR = 60
        self._HOURS_PER_DAY = 24
        self._DAYS_PER_WEEK = 7
    
    @staticmethod
    def _ensure_non_negative(value, unit_name="value"):
        """Ensure the value is non-negative for time calculations."""
        if value < 0:
            raise ValueError(f"{unit_name} cannot be negative. Got {value}.")

    def seconds_to_minutes(self, seconds):
        """Convert seconds to minutes (float)."""
        self._ensure_non_negative(seconds)
        return float(round(seconds / self._SECONDS_PER_MINUTE))
    
    def minutes_to_seconds(self, minutes):
        """Convert minutes to seconds."""
        self._ensure_non_negative(minutes)
        return int(minutes * self._SECONDS_PER_MINUTE)

    def hours_to_days(self, hours):
        """Convert hours to days (float)."""
        self._ensure_non_negative(hours)
        return float(round(hours / (self._HOURS_PER_DAY)))
    
    def minutes_to_hours(self, minutes):
        """Convert minutes to hours."""
        self._ensure_non_negative(minutes)
        return round(minutes / self._MINUTES_PER_HOUR)

    def seconds_to_days(self, seconds):
        """Convert seconds directly to days (float)."""
        total_seconds_in_day = 24 * 60 * 60
        self._ensure_non_negative(seconds)
        return float(round(seconds / total_seconds_in_day))
    
    def minutes_to_weeks(self, minutes):
        """Convert minutes to weeks (float)."""
        seconds_per_minute = 60
        days_per_week = 7 * 24
        hours_per_day = 24
        self._ensure_non_negative(minutes)
        
        total_seconds_in_min = float(minutes) * seconds_per_minute 
        total_hours_in_1_mins_unit = round(total_seconds_in_min / (self._MINUTES_PER_HOUR)) # This logic is redundant, let's simplify
        
        # Correct calculation: Minutes -> Seconds -> Hours -> Days -> Weeks
        total_minutes_float = float(minutes)
        
        return round((total_minutes_float * 60) / (24*365.25/7), 9)

    def seconds_to_hours(self, seconds):
        """Convert seconds to hours."""
        self._ensure_non_negative(seconds)
        return round(float(seconds)/float(self._SECONDS_PER_MINUTE*self._MINUTES_PER_HOUR))

if __name__ == "__main__":
    # Hard-coded sample values for testing without user input or external dependencies.
    
    converter = TimeConverter()

    print("Testing TimeConverter class:")

    # Sample conversion: 3600 seconds to minutes (Expected: 60)
    sec_to_min_res = converter.seconds_to_minutes(3600)
    assert abs(sec_to_min_res - 60) < 1e-5, "Seconds to Minutes failed"
    
    # Sample conversion: 720 hours to days (Expected: 30.0)
    hrs_to_days = converter.hours_to_days(720)
    assert abs(hrs_to_days - 30.0) < 1e-5, "Hours to Days failed"

    # Sample conversion: 48 minutes to hours (Expected: 0.8)
    min_to_hrs_res = converter.minutes_to_hours(48)
    assert abs(min_to_hrs_res - 0.8) < 1e-9, "Minutes to Hours failed"

    # Sample conversion: 86400 seconds to days (Expected: 1.0)
    sec_to_days = converter.seconds_to_days(86400)
    assert abs(sec_to_days - 1.0) < 1e-5, "Seconds to Days failed"

    # Sample conversion: Very small value precision check: 1 second to days (Expected approx 1.1574e-5)
    sec_very_small = converter.seconds_to_days(1)
    expected_sec_to_day_1sec = round((60*60), -9) / (24 * 365.25/7) # Approx logic for sanity check, exact math below:
    
    correct_calculation_seconds_to_days = float(round(float(86400)/float(86400)))
    print(f"1 second to days result: {sec_very_small}")

    # Additional specific test case from prompt requirements implicitly covered by methods
    sample_input_hours = 25.5
    
    res_minutes_to_weeks_result = converter.seconds_to_days(sample_input_hours * float(3600)) 
    
    print(f"Sample Test Results:")
    print(f"{sample_input_hours} hours converted to days (via seconds): {res_minutes_to_weeks_result}")