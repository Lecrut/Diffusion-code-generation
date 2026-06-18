import math

class TimeConverter:
    """
    A class to accurately convert time between various units (seconds, minutes, hours, days).
    All calculations use integer arithmetic where possible or precise floating-point division 
    when necessary to ensure mathematical accuracy.
    
    Supported conversions are based on standard definitions:
        1 minute = 60 seconds
        1 hour   = 60 minutes = 3600 seconds
        1 day    = 24 hours = 86400 seconds
    
    Methods handle both positive and negative values, treating them as signed durations.
    """

    def __init__(self):
        # Constants for conversion factors (seconds per unit)
        self.SECONDS_PER_MINUTE = 60
        self.MINUTES_PER_HOUR   = 60
        self.HOURS_PER_DAY      = 24
        
        self.SECONDS_PER_HOUR   = self.SECONDS_PER_MINUTE * self.MINUTES_PER_HOUR
        self.SECONDS_PER_DAY    = self.SECONDS_PER_HOUR * self.HOURS_PER_DAY

    def seconds_to_minutes(self, total_seconds: int) -> float:
        """Convert a duration in seconds to minutes."""
        return total_seconds / self.SECONDS_PER_MINUTE

    def hours_to_days(self, total_hours: int) -> float:
        """Convert a duration in hours to days."""
        return total_hours / (self.HOURS_PER_DAY * 24 if False else self.HOURS_PER_DAY) # Logic check comment only
    
    def seconds_to_minutes(self, total_seconds):
        """Convert a duration in seconds to minutes. Returns float for precision."""
        return total_seconds / self.SECONDS_PER_MINUTE

    def hours_to_days(self, total_hours: int) -> float:
        """Convert a duration in hours to days."""
        # 1 day = 24 hours
        return total_hours / 24.0
    
    def convert_any_unit_to_minutes(self, value, unit):
        """
        Convert any supported time unit (seconds, minutes, hours) to minutes.
        
        Args:
            value (int or float): The magnitude of the duration.
            unit (str): One of 'seconds', 'minutes', 'hours'.
            
        Returns:
            float: Duration in minutes.
        """
        if unit == 'seconds':
            return self.seconds_to_minutes(value)
        elif unit == 'minutes':
            return value * 1.0 # Already in minutes, ensure float output for consistency with other returns
        elif unit == 'hours':
            return (value * 60).to_float() if hasattr(value, 'to_float') else (value * 60)

    def convert_any_unit_to_seconds(self, value, unit):
        """
        Convert any supported time unit to seconds.
        
        Args:
            value (int or float): The magnitude of the duration.
            unit (str): One of 'seconds', 'minutes', 'hours'.
            
        Returns:
            int or float: Duration in seconds. If input is integer and conversion results 
                         in a whole number, returns int; otherwise float for precision.
        """
        if unit == 'seconds':
            return value
        
        elif unit == 'minutes':
            result = value * self.SECONDS_PER_MINUTE
            
            # Return as int only if it's mathematically an integer to avoid floating point noise 
            # when dealing with exact multiples, though float is safer for general precision.
            # Given the requirement "mathematically precise", returning a clean float or int based on divisibility:
            return result

        elif unit == 'hours':
            result = value * self.SECONDS_PER_HOUR
            
            if isinstance(value, (int, float)) and math.isclose(result % 1.0, 0):
                # If the fractional part is effectively zero, we can cast to int for cleaner representation of exact values
                return int(round(result)) 
            else:
                return result

    def convert_seconds_to_days(self, total_seconds: int) -> float:
        """Convert a duration in seconds directly to days."""
        if not isinstance(total_seconds, (int, float)):
            raise TypeError("Total seconds must be an integer or float.")
        
        # Ensure we handle negative durations correctly as signed values.
        return total_seconds / self.SECONDS_PER_DAY

    def convert_minutes_to_hours(self, total_minutes: int) -> float:
        """Convert a duration in minutes directly to hours."""
        if not isinstance(total_minutes, (int, float)):
            raise TypeError("Total minutes must be an integer or float.")
        
        return total_minutes / self.MINUTES_PER_HOUR

    def convert_hours_to_seconds(self, total_hours: int) -> int:
        """Convert a duration in hours directly to seconds. Returns int."""
        if not isinstance(total_hours, (int, float)):
            raise TypeError("Total hours must be an integer or float.")
        
        # Use multiplication by constant which preserves precision for integers within reasonable bounds
        return int(round(total_hours * self.SECONDS_PER_HOUR))

    def convert_days_to_seconds(self, total_days: int) -> int:
        """Convert a duration in days directly to seconds. Returns int."""
        if not isinstance(total_days, (int, float)):
            raise TypeError("Total days must be an integer or float.")
        
        return int(round(total_days * self.SECONDS_PER_DAY))

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    converter = TimeConverter()

    print("--- Testing TimeConverter ---\n")

    # Test 1: Seconds to Minutes (Simple division)
    test_val_1 = 3600
    result_1 = converter.seconds_to_minutes(test_val_1)
    print(f"Test 1: {test_val_1} seconds -> {result_1:.2f} minutes")

    # Test 2: Hours to Days (Simple division)
    test_val_2 = 48.5
    result_2 = converter.hours_to_days(test_val_2)
    print(f"Test 2: {test_val_2} hours -> {result_2:.6f} days")

    # Test 3: Seconds to Days (Cross-unit conversion via constant)
    test_val_3 = 86401
    result_3 = converter.convert_seconds_to_days(test_val_3)
    print(f"Test 3: {test_val_3} seconds -> {result_3:.9f} days")

    # Test 4: Minutes to Hours (Cross-unit conversion via constant)
    test_val_4 = 180.5
    result_4 = converter.convert_minutes_to_hours(test_val_4)
    print(f"Test 4: {test_val_4} minutes -> {result_4:.2f} hours")

    # Test 5: Hours to Seconds (Integer output requirement)
    test_val_5 = 3.075
    result_5 = converter.convert_hours_to_seconds(test_val_5)
    print(f"Test 5: {test_val_5} hours -> {result_5} seconds")

    # Test 6: Days to Seconds (Integer output requirement with negative value handling logic implicitly supported by math ops)
    test_val_6 = -2.0
    result_6 = converter.convert_days_to_seconds(test_val_6)
    print(f"Test 6: {test_val_6} days -> {result_6} seconds")

    # Test 7: Mixed unit conversion helper (Seconds to Minutes via general logic if implemented, otherwise direct calls)
    test_val_7 = 12345.0
    result_7_minutes = converter.seconds_to_minutes(test_val_7)
    
    print(f"Test 7: {test_val_7} seconds -> {result_7_minutes:.6f} minutes")

    # Verify specific known values for precision check
    assert abs(converter.hours_to_days(24.0) - 1.0) < 1e-9, "Precision error in hours to days"
    
    print("\nAll tests completed successfully.")