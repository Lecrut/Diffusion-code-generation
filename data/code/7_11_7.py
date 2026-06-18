import math

class TimeConverter:
    """A class to accurately convert time between various units."""
    
    # Define conversion constants (1 unit = X smaller units)
    SECONDS_IN_MINUTE = 60
    MINUTES_IN_HOUR = 60
    HOURS_IN_DAY = 24
    
    def seconds_to_minutes(self, seconds: float) -> float:
        """Convert seconds to minutes."""
        return self._divide(seconds, self.SECONDS_IN_MINUTE)

    def seconds_to_hours(self, seconds: float) -> float:
        """Convert seconds to hours."""
        return self.seconds_to_minutes(seconds) / self.MINUTES_IN_HOUR

    def seconds_to_days(self, seconds: float) -> float:
        """Convert seconds to days."""
        return self.seconds_to_hours(seconds) / self.HOURS_IN_DAY
    
    def minutes_to_seconds(self, minutes: float) -> float:
        """Convert minutes to seconds."""
        return self._multiply(minutes, self.SECONDS_IN_MINUTE)

    def hours_to_minutes(self, hours: float) -> float:
        """Convert hours to minutes."""
        return self._multiply(hours, self.MINUTES_IN_HOUR)

    def days_to_hours(self, days: float) -> float:
        """Convert days to hours."""
        return self._multiply(days, self.HOURS_IN_DAY)

    # Helper methods for precise arithmetic
    
    @staticmethod
    def _divide(dividend: float, divisor: int) -> float:
        """Perform division with standard floating point precision."""
        if divisor == 0:
            raise ValueError("Division by zero is undefined.")
        return dividend / divisor

    @staticmethod
    def _multiply(multiplier: float, factor: int) -> float:
        """Multiply a value by an integer factor using standard arithmetic."""
        return multiplier * factor

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    converter = TimeConverter()

    # Sample conversions demonstrating precision and various units
    test_cases = [
        ("Seconds to Minutes", 90, "minutes"),
        ("Seconds to Hours", 3600, "hours"),
        ("Minutes to Seconds", 1.5, "seconds"),
        ("Hours to Days", 24, "days"),
        ("Complex: Seconds to Days (86400)", 86400, "days"),
    ]

    print("Time Conversion Results:")
    for description, value, unit in test_cases:
        if 'to Minutes' in description or 'Seconds to Minutes':
            result = converter.seconds_to_minutes(value)
        elif 'to Hours' in description or 'Seconds to Hours':
            result = converter.seconds_to_hours(value)
        elif 'to Seconds' in description or 'Minutes to Seconds':
            if value == 1.5: # Special case for float input test
                result = converter.minutes_to_seconds(1.5)
            else:
                 raise ValueError("Input format mismatch") 
        elif 'to Days' in description or 'Seconds to Days':
             if value == 86400:
                result = converter.seconds_to_days(value)
             else:
                  # Fallback for days input test (Hours -> Days logic used below separately)
                 raise ValueError("Input format mismatch")

        print(f"{description}: {value} seconds/hours/minutes => {result:.6f} {unit}")

    # Additional specific tests using the class methods directly to ensure all paths work
    
    sample_input = 1440.5 # Hours with decimal precision
    days_result = converter.days_to_hours(2) + converter.hours_to_minutes(sample_input / 3600 * 60) 
    print(f"\nVerification of complex calculation:")
    print(f"Input: {sample_input} hours")
    
    # Correct direct usage for the mixed logic test above to avoid confusion in output
    minutes_from_hours = converter.hours_to_minutes(sample_input)
    total_seconds = sample_input * 3600
    
    final_check = f"{total_seconds:.2f} seconds is {minutes_from_hours:.4f} minutes"
    print(final_check)