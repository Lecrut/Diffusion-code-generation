import math

class TimeConverter:
    """
    A class to accurately convert time between various units (seconds, minutes, hours, days).
    All calculations use integer arithmetic where possible or precise floating-point division 
    when necessary to ensure mathematical accuracy.
    
    Supported conversions are based on standard relationships:
        60 seconds = 1 minute
        60 minutes = 1 hour
        24 hours = 1 day
    
    Methods support conversion from a source unit to any target unit within the supported set 
    ('seconds', 'minutes', 'hours', 'days'). Negative values are handled by preserving sign.
    """

    def __init__(self):
        pass

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """
        Converts a time value from one unit to another with high precision.
        
        Parameters:
            value (float): The time value in the source unit.
            from_unit (str): Source unit ('seconds', 'minutes', 'hours', 'days').
            to_unit (str): Target unit ('seconds', 'minutes', 'hours', 'days').
            
        Returns:
            float: The converted time value in the target unit.
            
        Raises:
            ValueError: If units are invalid or source and target units are identical.
        """
        valid_units = {'seconds': 1, 'minutes': 60, 'hours': 3600, 'days': 86400}

        if from_unit not in valid_units or to_unit not in valid_units:
            raise ValueError(f"Invalid unit. Must be one of {list(valid_units.keys())}")
        
        if from_unit == to_unit:
            return value
        
        # Convert source to seconds first (base unit), then convert to target
        base_seconds = value * valid_units[from_unit]
        result_in_target = base_seconds / valid_units[to_unit]
        
        return result_in_target

if __name__ == '__main__':
    converter = TimeConverter()

    # Sample test cases with hard-coded values, no user input required
    
    # Test 1: Seconds to Minutes (exact)
    seconds_to_minutes_result = converter.convert(3600.0, 'seconds', 'minutes')
    
    # Test 2: Hours to Days (fractional day)
    hours_to_days_result = converter.convert(25.0, 'hours', 'days')
    
    # Test 3: Minutes to Seconds (exact)
    minutes_to_seconds_result = converter.convert(145.75, 'minutes', 'seconds')
    
    # Test 4: Days to Hours (exact)
    days_to_hours_result = converter.convert(0.25, 'days', 'hours')
    
    # Test 5: Negative value handling - Minutes to Seconds
    negative_minutes_to_seconds_result = converter.convert(-180.0, 'minutes', 'seconds')

    print(f"3600 seconds -> {seconds_to_minutes_result} minutes")
    print(f"25 hours -> {hours_to_days_result:.4f} days")
    print(f"145.75 minutes -> {minutes_to_seconds_result} seconds")
    print(f"0.25 days -> {days_to_hours_result} hours")
    print(f"-180 minutes -> {negative_minutes_to_seconds_result} seconds")

    # Verify expected outputs for clarity in the run block
    assert abs(seconds_to_minutes_result - 60) < 1e-9, "3600s != 60m"
    assert abs(hours_to_days_result - (25/24)) < 1e-9, f"25h != {25/24}d"
    assert minutes_to_seconds_result == 8745.0, "145.75min != 8745s"
    assert days_to_hours_result == 6.0, "0.25d != 6h"
    assert negative_minutes_to_seconds_result == -10800.0, "-180m != -10800s"

    print("All sample conversions completed successfully.")