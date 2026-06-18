class TimeConverter:
    """A class to accurately convert time between various units."""
    
    # Define conversion constants (1 unit = X smaller units)
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    
    def seconds_to_minutes(self, total_seconds: float) -> float:
        """Convert total seconds to minutes."""
        return round(total_seconds / self.SECONDS_PER_MINUTE, 10)

    def seconds_to_hours(self, total_seconds: float) -> float:
        """Convert total seconds to hours."""
        return round(total_seconds / (self.SECONDS_PER_MINUTE * self.MINUTES_PER_HOUR), 10)

    def seconds_to_days(self, total_seconds: float) -> float:
        """Convert total seconds to days."""
        return round(total_seconds / (self.SECONDS_PER_MINUTE * self.MINUTES_PER_HOUR * self.HOURS_PER_DAY), 10)

    def minutes_to_hours(self, total_minutes: float) -> float:
        """Convert total minutes to hours."""
        return round(total_minutes / self.MINUTES_PER_HOUR, 10)

    def minutes_to_days(self, total_minutes: float) -> float:
        """Convert total minutes to days."""
        return round(total_minutes / (self.MINUTES_PER_HOUR * self.HOURS_PER_DAY), 10)

    def hours_to_days(self, total_hours: float) -> float:
        """Convert total hours to days."""
        return round(total_hours / self.HOURS_PER_DAY, 10)

    def minutes_to_seconds(self, total_minutes: float) -> int:
        """Convert total minutes to seconds (returns integer)."""
        return int(round(total_minutes * self.SECONDS_PER_MINUTE))

    def hours_to_seconds(self, total_hours: float) -> int:
        """Convert total hours to seconds (returns integer)."""
        return int(round(total_hours * self.MINUTES_PER_HOUR * self.SECONDS_PER_MINUTE))

    def days_to_seconds(self, total_days: float) -> int:
        """Convert total days to seconds (returns integer)."""
        return int(round(total_days * self.HOURS_PER_DAY * self.MINUTES_PER_HOUR * self.SECONDS_PER_MINUTE))

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    converter = TimeConverter()

    print("Time Conversion Results:")
    
    # Sample 1: Convert seconds to larger units
    sec_val = 3600.5
    print(f"\nInput: {sec_val} seconds")
    print(f"Minutes: {converter.seconds_to_minutes(sec_val)} minutes")
    print(f"Hours: {converter.seconds_to_hours(sec_val)} hours")
    print(f"Days: {converter.seconds_to_days(sec_val)} days")

    # Sample 2: Convert larger units to smaller units
    min_val = 145.75
    hour_val = 3.0
    
    print(f"\nInput: {min_val} minutes -> Seconds: {converter.minutes_to_seconds(min_val)} seconds")
    print(f"Input: {hour_val} hours -> Seconds: {converter.hours_to_seconds(hour_val)} seconds")

    # Sample 3: Complex conversions between days and hours/minutes
    day_val = 2.5
    
    print(f"\nInput: {day_val} days")
    print(f"Hours: {converter.days_to_seconds(day_val) / (60 * 60):.4f} hours") # Calculate manually for clarity or use helper if needed, but sticking to direct logic above
    # Let's recalculate using the class methods directly where possible
    
    days_in_hours = converter.hours_to_days(24.5)
    print(f"Input: {days_in_hours:.10f} hours -> Days: 2.5 (Verification)")

    # Direct day to seconds calculation for precision check
    total_seconds_from_2p5_days = converter.days_to_seconds(day_val)
    converted_back_minutes = total_seconds_from_2p5_days / 60
    print(f"Input: {day_val} days -> Seconds: {total_seconds_from_2p5_days}")
    print(f"Seconds back to Minutes: {converted_back_minutes:.4f} minutes")

    # Sample 4: Edge case with very small numbers
    tiny_sec = 0.1
    
    print(f"\nInput: {tiny_sec} seconds -> Hours: {converter.seconds_to_hours(tiny_sec)} hours")
    
    # Sample 5: Large number of days to years approximation (using the class logic)
    large_days = 365 * 24 * 70
    
    print(f"\nInput: {large_days} seconds -> Days: {converter.seconds_to_days(large_days)} days")